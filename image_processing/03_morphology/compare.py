"""Отдельная проверка по библиотекам — по последнему пункту задания."""

import cv2
import numpy as np
from scipy import ndimage
import morphology as m


def compare(image):
    kernel = np.ones((3, 3), dtype="uint8")
    binary = np.where(image > 127, 255, 0).astype("uint8")
    checks = [
        ("erosion", m.erosion(image, kernel), cv2.erode(image, kernel)),
        ("dilation", m.dilation(image, kernel), cv2.dilate(image, kernel)),
        ("opening", m.opening(image, kernel), cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)),
        ("closing", m.closing(image, kernel), cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)),
        ("contour", m.contour(image, kernel), image - cv2.erode(image, kernel)),
        ("gradient", m.gradient(image, kernel), cv2.morphologyEx(image, cv2.MORPH_GRADIENT, kernel)),
        ("white_top_hat", m.white_top_hat(image, kernel), cv2.morphologyEx(image, cv2.MORPH_TOPHAT, kernel)),
        ("black_top_hat", m.black_top_hat(image, kernel), cv2.morphologyEx(image, cv2.MORPH_BLACKHAT, kernel)),
    ]
    for name, function, code in [("zhang_suen", m.zhang_suen, cv2.ximgproc.THINNING_ZHANGSUEN),
                                  ("guo_hall", m.guo_hall, cv2.ximgproc.THINNING_GUOHALL)]:
        # OpenCV не обрабатывает край: добавляем рамку и убираем её после.
        reference = cv2.ximgproc.thinning(np.pad(binary, 1), thinningType=code)[1:-1, 1:-1]
        checks.append((name, function(binary), reference))
    heights = np.array([[0, 1, 0], [1, 2, 1], [0, 1, 0]])
    gray = image.astype(int)
    checks += [
        ("nonflat_erosion", m.erosion(image, kernel, heights=heights),
         ndimage.grey_erosion(gray, structure=heights, mode="constant", cval=255)),
        ("nonflat_dilation", m.dilation(image, kernel, heights=heights),
         ndimage.grey_dilation(gray, structure=heights, mode="constant", cval=0)),
    ]
    cross = np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]], dtype="uint8")
    current = binary.copy()
    skeleton = np.zeros_like(binary)
    while current.any():
        eroded = cv2.erode(current, cross, borderType=cv2.BORDER_CONSTANT, borderValue=0)
        restored = cv2.dilate(eroded, cross, borderType=cv2.BORDER_CONSTANT, borderValue=0)
        skeleton = np.maximum(skeleton, current - restored)
        current = eroded
    checks.append(("skeleton", m.morphological_skeleton(binary), skeleton))
    for name, own, reference in checks:
        different = np.count_nonzero(own != reference)
        print(f"{name}: несовпадающих пикселей — {different}")
        assert different == 0, name


if __name__ == "__main__":
    from main import folder
    image = cv2.imread(str(folder / "binary_image.png"), cv2.IMREAD_GRAYSCALE)
    if image is None:
        raise FileNotFoundError("Не найден binary_image.png")
    compare(image)
