import cv2
import numpy as np
from  matplotlib import pyplot as plt

img = cv2.imread("1.jpg",0)
dst = cv2.resize(img,(512,512))
dst = np.array(dst,dtype=np.float)
d = 512
ds = np.zeros((512,512))
for i in range(d/2):
  for j in range(d/2):
    j2 = 2*j
    ds[i,j]=(dst[i,j2]+dst[i,j2+1]+dst[i+1,j2]+dst[i+1,j2])*0.25
    ds[i,j+d/2]=(dst[i,j2]-dst[i,j2+1]+dst[i+1,j2]-dst[i+1,j2])*0.25
    ds[i+d/2,j]=(dst[i,j2]+dst[i,j2+1]-dst[i+1,j2]-dst[i+1,j2])*0.25
    ds[i+d/2,j+d/2]=(dst[i,j2]-dst[i,j2+1]-dst[i+1,j2]+dst[i+1,j2])*0.25

ds = np.array(ds,dtype=np.uint8)
plt.imshow(ds,cmap="gray")
plt.show()
