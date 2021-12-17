import cv2
import numpy as np
image = cv2.imread('Images/Parking_5.jpg')
output = image.copy()
img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
img = cv2.GaussianBlur(img, (21,21), cv2.BORDER_DEFAULT) 
# Find circles
circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT,0.9,120,param1 =50, param2 = 30 , minRadius= 60, maxRadius=100)
# If some circle is found
if circles is not None:
   # Get the (x, y, r) as integers
   circles = np.round(circles[0, :]).astype("int")
   print(circles)
   # loop over the circles
   for (x, y, r) in circles:
      cv2.circle(output, (x, y), r, (0, 255, 0), 2)
# show the output image
cv2.imshow("circle",output)
cv2.waitKey(0)