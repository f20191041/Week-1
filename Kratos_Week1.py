import numpy as np
import matplotlib.pyplot as plt

n_rows = int(input('INPUR NUMBER OF ROWS\n'))

img = np.zeros((n_rows, n_rows ,3) , dtype= np.uint8)
n = 255.0/500.0
i=0
for k in range(i, n_rows-i):
    img[k,i:n_rows-i] = n*i
    img[i:n_rows-i, k] = n*i
    img[i:n_rows-i,n_rows-k-1] = n*i
    img[n_rows-k-1, i:n_rows-i] = n*i
    i+=1

plt.imshow(img)
plt.show()

