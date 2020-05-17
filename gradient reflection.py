import numpy as np
import matplotlib.pyplot as plt 
grad=np.zeros((1000,1000,3),dtype=np.uint8)
val=np.linspace(0,255,500)
for x in range(500):
    grad[x:1000-x,x:1000-x]=val[x]
plt.imshow(grad)
plt.show()
#print(grad)
