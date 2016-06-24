import numpy as np
from matplotlib import pyplot as plt
import cv2

img = cv2.imread("lena512.bmp")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray,(3,3),0.4)
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

magnitude = np.hypot(Ix, Iy)
angle = np.arctan2(Iy, Ix)*180/np.pi


#nonmax_suppression
for x in range(r):
    for y in range(c):
        if (angle[x][y]<22.5 and angle[x][y]>=-22.5) or \
           (angle[x][y]>=157.5) or \
           (angle[x][y]<=-157.5 ):
            angle[x][y]=0
        elif (angle[x][y]>=22.5 and angle[x][y]<67.5) or \
             (angle[x][y]>=-67.6 and angle[x][y]<-22.5):
            angle[x][y]=45
        elif (angle[x][y]>=67.5 and angle[x][y]<112.5)or \
             (angle[x][y]>=-112.5 and angle[x][y]<-67.5):
            angle[x][y]=90
        else:
            angle[x][y]=135




mag_sup = magnitude.copy()

for x in range(1, r-1):
    for y in range(1, c-1):
        if angle[x][y]==0:
            if (magnitude[x][y]<=magnitude[x][y+1]) or \
               (magnitude[x][y]<=magnitude[x][y-1]):
                mag_sup[x][y]=0
        elif magnitude[x][y]==45:
            if (magnitude[x][y]<=magnitude[x-1][y+1]) or \
               (magnitude[x][y]<=magnitude[x+1][y-1]):
                mag_sup[x][y]=0
        elif angle[x][y]==90:
            if (magnitude[x][y]<=magnitude[x+1][y]) or \
               (magnitude[x][y]<=magnitude[x-1][y]):
                mag_sup[x][y]=0
        else:
            if (magnitude[x][y]<=magnitude[x+1][y+1]) or \
               (magnitude[x][y]<=magnitude[x-1][y-1]):
                mag_sup[x][y]=0



m = np.max(mag_sup)
th = 0.2*m
tl = 0.1*m


high = np.zeros((r, c))
low = np.zeros((r, c))

for x in range(r):
    for y in range(c):
        if mag_sup[x][y]>=th:
            high[x][y]=mag_sup[x][y]
        if mag_sup[x][y]>=tl:
            low[x][y]=mag_sup[x][y]

low = low-high



def traverse(i, j):
    x = [-1, 0, 1, -1, 1, -1, 0, 1]
    y = [-1, -1, -1, 0, 0, 1, 1, 1]
    for k in range(8):
        if high[i+x[k]][j+y[k]]==0 and low[i+x[k]][j+y[k]]!=0:
            high[i+x[k]][j+y[k]]=1
            traverse(i+x[k], j+y[k])

for i in range(1, r-1):
    for j in range(1, c-1):
        if high[i][j]:
            high[i][j]=1
            traverse(i, j)

plt.imshow(high,cmap="gray")

plt.show()
