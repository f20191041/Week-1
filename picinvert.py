import urllib.request 
from PIL import Image 
import numpy as np
url = 'https://images-na.ssl-images-amazon.com/images/I/81KA4Aty8xL._SL1000_.jpg'
image = Image.open(urllib.request.urlopen(url))
dat = np.asarray(image,dtype="int32")
dat1=255-dat
img=Image.fromarray(dat1, 'RGB')
img.save("invertpic.png")
img.show()
