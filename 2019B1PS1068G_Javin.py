import numpy as np
# Function to plot image:
import matplotlib.pyplot as plot
import time

print("Hello! Program is loading(give it 8 secs) ")
# Creating a 1000x1000 black image
arr = np.zeros((1000, 1000, 3), dtype=np.int16)
img_size = (1000, 1000)
colour_edge = (0, 0, 0)  # Black pixel
colour_center = (255, 255, 255)  # White pixel

for x in range(1000):
    for y in range(1000):
        # Using formula dst b/w 2 points
        edge_dst = np.sqrt((x - 500) ** 2 + (y - 500) ** 2)
        # Convering to decimal b/w 0-1
        edge_dst = float(edge_dst) / (np.sqrt(2) * 500)

        # Calculating intensity
        intensity = 255 * (1 - edge_dst)
        arr[x, y] = (int(intensity), int(intensity), int(intensity))


plot.imshow(arr)
plot.show()
