# "iNNovationMerge DailyCodeHub"

# Python program to display an image in color spaces using OpenCV split() Method

# pip install opencv-python
import cv2
import os 

# Read PNG Image 
Image = cv2.imread("iNNovationMerge.JPG") 

# Corresponding channels are seperated 
B, G, R = cv2.split(Image) 

# Display original color image
cv2.imshow("original", Image) 
cv2.waitKey(0) 
  
# Display blue color image
cv2.imshow("blue", B) 
cv2.waitKey(0) 
  
# Display Green color image
cv2.imshow("Green", G) 
cv2.waitKey(0) 
  
cv2.imshow("red", R) 
cv2.waitKey(0) 
  
#closing all open windows 
cv2.destroyAllWindows() 