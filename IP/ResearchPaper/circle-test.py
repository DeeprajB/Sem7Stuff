import cv2
import numpy as np
import matplotlib.pyplot as plt

image = "Images/Parking_Full.jpg"
img = cv2.imread(image,1)
img_crig = img.copy()
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

img = cv2.GaussianBlur(img, (21,21), cv2.BORDER_DEFAULT) 

all_circs = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT,0.9,120,param1 =50, param2 = 30 , minRadius= 60, maxRadius=100)
all_circs_rounded = np.uint16(np.around(all_circs))

print(all_circs_rounded)
print(all_circs_rounded.shape)
print("i Have found"+ str(all_circs_rounded.shape[1])+ 'coins')
