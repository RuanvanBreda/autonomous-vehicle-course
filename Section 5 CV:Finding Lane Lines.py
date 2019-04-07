#pip install opencv-contrib-python
import cv2

image = cv2.imread('Image/test_image.jpg')
cv2.imshow('result',image)
cv2.waitKey(0)  #Displays image untill further input is received