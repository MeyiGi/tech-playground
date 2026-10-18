import cv2
import matplotlib.pyplot as plt

im = cv2.imread('image_for_equalizer.png', 0)
result = cv2.equalizeHist(im)

for i, image in enumerate([im, result]):
    plt.subplot(2, 2, i + 1)
    plt.imshow(image, cmap='gray', vmin=0, vmax=255)
    plt.title(['До', 'После'][i])
    plt.subplot(2, 2, i + 3)
    plt.hist(image.flatten(), 256, (0, 256))

plt.show()
