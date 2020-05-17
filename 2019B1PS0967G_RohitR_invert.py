from skimage import io
import numpy as np
import matplotlib.pyplot as plt

img = io.imread('colors.jpg')

img[: ,: ,: ] = 255 - img[: ,: ,: ]

plt.imshow(img)