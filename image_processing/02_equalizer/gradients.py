import cv2
import numpy as np
import matplotlib.pyplot as plt

im = cv2.imread('image_for_equalizer.png', 0)
h, w = im.shape

# Градиенты от 0 до 1.
horizontal = np.tile(np.linspace(0, 1, w), (h, 1))
vertical = np.tile(np.linspace(0, 1, h).reshape(h, 1), (1, w))
diagonal = (horizontal + vertical) / 2

for i, mask in enumerate([horizontal, vertical, diagonal]):
    # Умножение меняет контраст, прибавление — яркость.
    result = im * (0.5 + mask) + 80 * mask - 40
    result = np.clip(result, 0, 255).astype(np.uint8)

    plt.subplot(1, 3, i + 1)
    plt.imshow(result, cmap='gray', vmin=0, vmax=255)
    plt.title(['Горизонталь', 'Вертикаль', 'Диагональ'][i])
    plt.axis('off')

plt.show()
