#pip install opencv-contrib-python
import cv2
import numpy as np

image = cv2.imread('Image/test_image.jpg')
lane_image = image  #Make a copy of original image


#Edge Detection using changes in intensity [0-255]
#Rapid change in pixel density
gray_image = cv2.cvtColor(lane_image,cv2.COLOR_RGB2GRAY) #Grayscale Conversion
cv2.imshow('result',gray_image)
cv2.waitKey(0)  #Displays image untill further input is received

