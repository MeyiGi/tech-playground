"""Учебные операции над двумерными изображениями, независимо от GUI."""

from pathlib import Path

import cv2
import numpy as np


# Ядра математической СВЁРТКИ. После переворота внутри convolve2d
# положительный Gx означает рост яркости вправо, Gy — вниз (координаты экрана).
SOBEL_X = np.array([[1, 0, -1], [2, 0, -2], [1, 0, -1]], dtype=float)
SOBEL_Y = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]], dtype=float)
LAPLACIAN = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]], dtype=float)


def convolve2d(gray, kernel):
    """Настоящая свёртка 3×3: переворот ядра, окно, сумма произведений.

    Края продолжаем ближайшим пикселем (edge). Результат сохраняет H×W.
    Float64 предотвращает переполнение uint8 и сохраняет знак производной.
    """
    gray = np.asarray(gray, dtype=np.float64)
    kernel = np.asarray(kernel, dtype=np.float64)
    if gray.ndim != 2 or gray.size == 0:
        raise ValueError("Нужна непустая двумерная матрица.")
    if kernel.shape != (3, 3):
        raise ValueError("Нужно ядро 3×3.")
    padded = np.pad(gray, 1, mode="edge")
    flipped = kernel[::-1, ::-1]  # Поворот на 180° отличает свёртку от корреляции.
    result = np.zeros_like(gray)
    height, width = gray.shape
    for y in range(height):
        for x in range(width):
            patch = padded[y:y + 3, x:x + 3]
            # Девять произведений «яркость × вес», затем их сумма.
            result[y, x] = np.sum(patch * flipped)
    return result


def normalize(values):
    """Линейно переводим неотрицательную силу отклика в 0…255."""
    values = np.asarray(values, dtype=np.float64)
    maximum = float(values.max())
    if maximum == 0:
        return np.zeros(values.shape, dtype=np.uint8)
    return np.clip(values / maximum * 255, 0, 255).round().astype(np.uint8)


def derivatives(gray):
    gx = convolve2d(gray, SOBEL_X)
    gy = convolve2d(gray, SOBEL_Y)
    # Для КАЖДОГО пикселя: sqrt(Gx² + Gy²); исходные знаки сохранены.
    magnitude = np.sqrt(gx ** 2 + gy ** 2)
    laplacian = convolve2d(gray, LAPLACIAN)
    return {"gx": gx, "gy": gy, "magnitude": magnitude,
            "sobel": normalize(magnitude),
            "laplacian_raw": laplacian,
            "laplacian": normalize(np.abs(laplacian))}


def canny(gray, low=50, high=150):
    if not 0 <= low < high <= 255:
        raise ValueError("Пороги должны удовлетворять 0 ≤ нижний < верхний ≤ 255.")
    # Сглаживание подавляет шум до поиска градиентов. L2gradient использует
    # евклидов модуль sqrt(Gx² + Gy²), а не сумму модулей компонент.
    blurred = cv2.GaussianBlur(gray, (5, 5), 1.0, borderType=cv2.BORDER_REPLICATE)
    return cv2.Canny(blurred, low, high, apertureSize=3, L2gradient=True)


def load_image(path):
    # imdecode/fromfile работают и с кириллицей в пути на Windows.
    data = np.fromfile(Path(path), dtype=np.uint8)
    bgr = cv2.imdecode(data, cv2.IMREAD_COLOR)
    if bgr is None:
        raise ValueError("Не удалось прочитать изображение. Выберите PNG, JPEG или BMP.")
    rgb = cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)
    gray = cv2.cvtColor(bgr, cv2.COLOR_BGR2GRAY)
    return rgb, gray


def save_image(path, pixels):
    suffix = Path(path).suffix.lower()
    if suffix not in {".png", ".jpg", ".jpeg", ".bmp"}:
        raise ValueError("Выберите расширение PNG, JPEG или BMP.")
    ok, encoded = cv2.imencode(suffix, pixels)
    if not ok:
        raise ValueError("Не удалось закодировать изображение.")
    encoded.tofile(Path(path))
