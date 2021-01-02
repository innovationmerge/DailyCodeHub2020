# "iNNovationMerge DailyCodeHub"

# Python program to display an image using OpenCV imshow() Method

# pip install opencv-python
import cv2
import os 

# Read PNG Image 
PNGImage = cv2.imread("iNNovationMerge.png") 

# Display image
cv2.imshow("iNNovationMerge.png", PNGImage) 

# Wait for user input
cv2.waitKey(0)  

#closing all open windows  
cv2.destroyAllWindows()  