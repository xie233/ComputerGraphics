import  cv2
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread("lena512.bmp")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
Gx = [[-1,0,1],
           [-2,0,2],
           [-1,0,1]]
Gy = [[-1,-2,-1],
           [0,0,0],
           [1,2,1]]
r = gray.shape[0]
c = gray.shape[1]
Ix = np.zeros((r,c))
Iy = np.zeros((r,c))
for x in range(1, r-1):
    for y in range(1, c-1):
        px = (Gx[0][0] * gray[x-1][y-1]) + (Gx[0][1] * gray[x][y-1]) + \
             (Gx[0][2] * gray[x+1][y-1]) + (Gx[1][0] * gray[x-1][y]) + \
             (Gx[1][1] * gray[x][y]) + (Gx[1][2] * gray[x+1][y]) + \
             (Gx[2][0] * gray[x-1][y+1]) + (Gx[2][1] * gray[x][y+1]) + \
             (Gx[2][2] * gray[x+1][y+1])

        py = (Gy[0][0] * gray[x-1][y-1]) + (Gy[0][1] * gray[x][y-1]) + \
             (Gy[0][2] * gray[x+1][y-1]) + (Gy[1][0] * gray[x-1][y]) + \
             (Gy[1][1] * gray[x][y]) + (Gy[1][2] * gray[x+1][y]) + \
             (Gy[2][0] * gray[x-1][y+1]) + (Gy[2][1] * gray[x][y+1]) + \
             (Gy[2][2] * gray[x+1][y+1])
        Ix[x][y] = px
        Iy[x][y] = py

Ixx = np.dot(Ix,Ix)
Iyy = np.dot(Iy,Iy)
Ixy = np.dot(Ix,Iy)

Sxx = cv2.GaussianBlur(Ixx,(3,3),0.3)
Syy = cv2.GaussianBlur(Iyy,(3,3),0.3)
Sxy = cv2.GaussianBlur(Ixy,(3,3),0.3)
print Sxx.shape
HR = np.zeros((r,c))
k=0.03
for i in range(r):
    for j in range(c):
        d = (Sxx[i,j]*Syy[i,j]-Sxy[i,j]*Sxy[i,j])-k*(Sxx[i,j]+Syy[i,j])*(Sxx[i,j]+Syy[i,j])
        HR[i,j] = d


max = HR.max()
count = np.zeros((r,c))
#nonmax suppression
th = 0.15
corner = 0
for m in range(1,r-1):
    for n in range(1,c-1):
        if HR[m,n]>th*max and HR[m,n]>HR[m,n-1] and HR[m,n]>HR[m,n+1] and (HR[m,n]>
            HR[m-1,n]) and HR[m,n]>HR[m+1,n] and HR[m,n]>HR[m-1,n-1] and (HR[m,n]>
                HR[m-1,n+1]) and HR[m,n]>HR[m+1,n-1] and HR[m+1,n+1]:
            count[m,n] = 1
            corner = corner+1

d = np.where(count==1)
dx,dy = d
plt.imshow(gray,cmap="gray")
plt.plot(dx,dy,'*')
plt.axis("off")
plt.show()

