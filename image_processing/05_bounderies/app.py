"""Запуск: python app.py. Выберите картинку и посмотрите результат."""

import tkinter as tk
from tkinter import filedialog, messagebox

import matplotlib.pyplot as plt
import numpy as np

from processing import SOBEL_X, SOBEL_Y, convolve2d, load_image, normalize


def gradient_and_edges(gray, threshold=50):
    gx = convolve2d(gray, SOBEL_X)  # Изменение яркости по горизонтали.
    gy = convolve2d(gray, SOBEL_Y)  # Изменение яркости по вертикали.
    magnitude = np.sqrt(gx ** 2 + gy ** 2)  # Модуль для каждого пикселя.
    gradient = normalize(magnitude)  # Яркость от 0 до 255 для показа.
    edges = (gradient > threshold).astype(np.uint8) * 255
    return gradient, edges


def main():
    root = tk.Tk()
    root.withdraw()
    path = filedialog.askopenfilename(
        title="Выберите изображение",
        filetypes=[("Изображения", "*.png *.jpg *.jpeg *.bmp"),
                   ("Все файлы", "*")],
    )
    if not path:
        root.destroy()
        return

    try:
        original, gray = load_image(path)
    except (OSError, ValueError) as error:
        messagebox.showerror("Ошибка", str(error))
        root.destroy()
        return
    root.destroy()

    gradient, edges = gradient_and_edges(gray)
    figure, axes = plt.subplots(1, 3, figsize=(12, 4))
    for ax, pixels, title in zip(
        axes, [original, gradient, edges],
        ["Оригинал", "Модуль градиента", "Границы"],
    ):
        ax.imshow(pixels, cmap="gray", vmin=0, vmax=255)
        ax.set_title(title)
        ax.axis("off")
    figure.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
