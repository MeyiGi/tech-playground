import cv2
import numpy as np
import matplotlib.pyplot as plt


image = cv2.imread("data/cat_image.jpg", cv2.IMREAD_GRAYSCALE)
if image is None:
    raise SystemExit("Не найдена картинка data/cat_image.jpg")

# Уменьшаем картинку, чтобы циклы работали быстрее.
image = cv2.resize(image, (500, 500))

kernel_x = np.array([[1, 0, -1], [2, 0, -2], [1, 0, -1]])
kernel_y = kernel_x.T

height, width = image.shape
padded = np.pad(image.astype(float), 1, mode="edge")
gradient = np.zeros((height, width))

for y in range(height):
    for x in range(width):
        window = padded[y:y + 3, x:x + 3]
        # Для свёртки переворачиваем ядра.
        gx = np.sum(window * kernel_x[::-1, ::-1])
        gy = np.sum(window * kernel_y[::-1, ::-1])
        gradient[y, x] = np.sqrt(gx ** 2 + gy ** 2)

# Переводим модуль градиента в яркость от 0 до 255.
if gradient.max() > 0:
    gradient = gradient / gradient.max() * 255

edges = (gradient > 50) * 255

plt.figure(figsize=(12, 4))
for i, (picture, title) in enumerate([
    (image, "Оригинал"), (gradient, "Градиент"), (edges, "Границы")
]):
    plt.subplot(1, 3, i + 1)
    plt.imshow(picture, cmap="gray", vmin=0, vmax=255)
    plt.title(title)
    plt.axis("off")

plt.tight_layout()
plt.show()
