"""Решение домашней работы. Морфология реализована в morphology.py."""

from pathlib import Path
import cv2
import numpy as np
import morphology as m


# OpenCV здесь только читает и сохраняет файлы.
folder = Path(__file__).resolve().parent


def main():
    image = cv2.imread(str(folder / "binary_image.png"), cv2.IMREAD_GRAYSCALE)
    if image is None:
        raise FileNotFoundError("Не найден binary_image.png")
    # min/max работают и с полутонами. Для thinning нужен бинарный вход.
    binary = np.where(image > 127, 255, 0)
    kernel = np.ones((3, 3), dtype=int)
    heights = np.array([[0, 1, 0], [1, 2, 1], [0, 1, 0]])
    results = {
        "original": image,
        "erosion": m.erosion(image, kernel),
        "dilation": m.dilation(image, kernel),
        "opening": m.opening(image, kernel),
        "closing": m.closing(image, kernel),
        "contour": m.contour(image, kernel),
        "gradient": m.gradient(image, kernel),
        "white_top_hat": m.white_top_hat(image, kernel),
        "black_top_hat": m.black_top_hat(image, kernel),
        "zhang_suen": m.zhang_suen(binary),
        "guo_hall": m.guo_hall(binary),
        "skeleton": m.morphological_skeleton(binary),
        "nonflat_erosion": m.erosion(image, kernel, heights=heights),
        "nonflat_dilation": m.dilation(image, kernel, heights=heights),
    }
    output = folder / "results"
    output.mkdir(exist_ok=True)
    for name, result in results.items():
        # Только при сохранении ограничиваем яркость диапазоном PNG.
        cv2.imwrite(str(output / f"{name}.png"), np.clip(result, 0, 255).astype("uint8"))
    print("Результаты сохранены в", output)


if __name__ == "__main__":
    main()
