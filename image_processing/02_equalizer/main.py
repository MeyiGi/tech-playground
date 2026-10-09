import matplotlib.pyplot as plt
import cv2
import numpy as np


# Build histogram of current image
im = cv2.imread('./image_for_equalizer.png')
# calculate mean value from RGB channels and flatten to 1D array
vals = im.mean(axis=2).flatten()
# plot histogram with 255 bins
b, bins, patches = plt.hist(vals, 255)
plt.xlim([0,255])
plt.show()


# (CDF) for calculating cumilative distribution function
cdf = np.cumsum(np.histogram(vals, 256, (0, 256))[0])
plt.plot(cdf); 
plt.show()