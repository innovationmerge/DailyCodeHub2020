# "iNNovationMerge DailyCodeHub"

# Python program to erode an image using OpenCV

# pip install opencv-python  
 
import cv2 
import numpy as np 

# Read the image 
image = cv2.imread("iNNovationMerge.jpg", 1) 

# Window name in which image is displayed  
window_name = 'iNNovationMerge'
  
# Creating kernel 
kernel = np.ones((5, 5), np.uint8) 
  
# Using cv2.erode() method  
image = cv2.erode(image, kernel)  
  
# Displaying the image  
cv2.imshow(window_name, image)  
cv2.waitKey(0) 