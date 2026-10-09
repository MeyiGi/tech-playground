import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('binary_image.png', 0)

kernel_erosion = np.ones((3, 3), np.uint8)
kernel_dilitation = np.zeros((3, 3), np.uint8)

img_erosion = cv2.erode(img, kernel_erosion, iterations=1)
img_closing = cv2.dilate(img_erosion, kernel_dilitation, iterations=1)

plt.figure(figsize=(10, 5))

plt.subplot(1, 3, 1)
plt.imshow(img, cmap='gray')
plt.title("Original Image")

plt.subplot(1, 3, 2)
plt.imshow(img_erosion, cmap='gray')
plt.title("After Erosion")

plt.subplot(1, 3, 3)
plt.imshow(img_closing, cmap='gray')
plt.title("After Closing")

plt.tight_layout()
plt.show()