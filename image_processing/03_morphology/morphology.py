"""Алгоритмы вручную. Из библиотек здесь только NumPy для массивов."""

import numpy as np


def erosion(image, kernel, border=255, heights=None):
    # В каждой окрестности берём минимальную яркость.
    h, w = image.shape
    kh, kw = kernel.shape
    padded = np.pad(image.astype(int), ((kh // 2, kh // 2), (kw // 2, kw // 2)),
                    constant_values=border)
    result = np.zeros((h, w), dtype=int)
    for y in range(h):
        for x in range(w):
            window = padded[y:y + kh, x:x + kw]
            if heights is not None:
                window = window - heights
            result[y, x] = min(window[kernel == 1])
    return result


def dilation(image, kernel, heights=None):
    # В каждой окрестности берём максимальную яркость.
    h, w = image.shape
    kh, kw = kernel.shape
    padded = np.pad(image.astype(int), ((kh // 2, kh // 2), (kw // 2, kw // 2)))
    result = np.zeros((h, w), dtype=int)
    if heights is not None:
        # Для неплоской дилатации отражаем структурный элемент.
        heights = heights[::-1, ::-1]
        kernel = kernel[::-1, ::-1]
    for y in range(h):
        for x in range(w):
            window = padded[y:y + kh, x:x + kw]
            if heights is not None:
                window = window + heights
            result[y, x] = max(window[kernel == 1])
    return result


def opening(image, kernel):
    return dilation(erosion(image, kernel), kernel)


def closing(image, kernel):
    return erosion(dilation(image, kernel), kernel)


def contour(image, kernel):
    return image - erosion(image, kernel)


def gradient(image, kernel):
    return dilation(image, kernel) - erosion(image, kernel)


def white_top_hat(image, kernel):
    return image - opening(image, kernel)


def black_top_hat(image, kernel):
    return closing(image, kernel) - image


def thinning(image, method="zhang_suen"):
    # 0 — фон, 1 — объект. Рамка нужна для соседей крайних пикселей.
    result = np.pad((image > 0).astype(int), 1)
    while True:
        changed = False
        for step in (0, 1):
            to_delete = []
            for y, x in np.argwhere(result == 1):
                # Соседи по часовой стрелке, начиная сверху.
                p2 = result[y - 1, x]
                p3 = result[y - 1, x + 1]
                p4 = result[y, x + 1]
                p5 = result[y + 1, x + 1]
                p6 = result[y + 1, x]
                p7 = result[y + 1, x - 1]
                p8 = result[y, x - 1]
                p9 = result[y - 1, x - 1]

                if method == "zhang_suen":
                    neighbors = [p2, p3, p4, p5, p6, p7, p8, p9, p2]
                    count = sum(neighbors[:8])
                    transitions = 0
                    for i in range(8):
                        if neighbors[i] == 0 and neighbors[i + 1] == 1:
                            transitions += 1
                    if step == 0:
                        direction = p2 * p4 * p6 == 0 and p4 * p6 * p8 == 0
                    else:
                        direction = p2 * p4 * p8 == 0 and p2 * p6 * p8 == 0
                    remove = 2 <= count <= 6 and transitions == 1 and direction
                else:  # Guo–Hall: формулы со слайда 23.
                    c = sum([not p2 and (p3 or p4), not p4 and (p5 or p6),
                             not p6 and (p7 or p8), not p8 and (p9 or p2)])
                    n1 = sum([p9 or p2, p3 or p4, p5 or p6, p7 or p8])
                    n2 = sum([p2 or p3, p4 or p5, p6 or p7, p8 or p9])
                    n = min(n1, n2)
                    if step == 0:
                        m = (p6 or p7 or not p9) and p8
                    else:
                        m = (p2 or p3 or not p5) and p4
                    remove = c == 1 and 2 <= n <= 3 and not m

                if remove:
                    to_delete.append((y, x))
            # Удаляем одновременно, когда проверили все пиксели подшага.
            for y, x in to_delete:
                result[y, x] = 0
            if to_delete:
                changed = True
        if not changed:
            return result[1:-1, 1:-1] * 255


def zhang_suen(image):
    return thinning(image, "zhang_suen")


def guo_hall(image):
    return thinning(image, "guo_hall")


def morphological_skeleton(image):
    kernel = np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]])
    current = np.where(image > 0, 255, 0)
    skeleton = np.zeros_like(current)
    while current.any():
        eroded = erosion(current, kernel, border=0)
        restored = dilation(eroded, kernel)
        skeleton = np.maximum(skeleton, current - restored)
        current = eroded
    return skeleton
