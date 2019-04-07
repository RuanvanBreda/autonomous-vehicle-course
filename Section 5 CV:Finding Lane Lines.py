#pip install opencv-contrib-python
import cv2
import numpy as np

image = cv2.imread('Image/test_image.jpg')
lane_image = image  #Make a copy of original image


#Edge Detection using changes in intensity [0-255]
#Rapid change in pixel density
gray_image = cv2.cvtColor(lane_image,cv2.COLOR_RGB2GRAY) #Grayscale Conversion

#Smooth Image using Gaussian Blurr to reduce noise - noise can create false edges - use a kernel
blur_image = cv2.GaussianBlur(gray_image,(5,5),0)   #original image, size of kernel, deviation

cv2.imshow('result',blur_image)
cv2.waitKey(0)  #Displays image untill further input is received