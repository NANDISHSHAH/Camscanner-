import cv2
import numpy as np 
image=cv2.imread("car.jpg")
image=cv2.resize(image,(1300,800))
orig=image.copy()
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow("gray",gray)
cv2.waitKey(0)
blurred=cv2.GaussianBlur(gray,(5,5),0)
cv2.imshow("blurred",blurred)
cv2.waitKey(0)
edged=cv2.Canny(blurred,3,5)
cv2.imshow('edged',edged)
cv2.waitKey(1)
 