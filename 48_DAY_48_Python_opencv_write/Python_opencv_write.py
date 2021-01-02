# "iNNovationMerge DailyCodeHub"

# Python program to write an image using OpenCV imwrite() Method

# pip install opencv-python
import cv2
import os 

# Read PNG Image 
PNGImage = cv2.imread("iNNovationMerge.png") 

# Write image as PNGImage
cv2.imwrite("iNNovationMerge.jpg", PNGImage) 
