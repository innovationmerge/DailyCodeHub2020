# **************** "iNNovationMerge DailyCodeHub" ****************
# Visit https://www.innovationmerge.com/
# Theme : Week with image preprocessing using OpenCV

# Python program for converting colour image to grayscale image

import cv2
import os 
image = cv2.imread('test.JPG')
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite('test_output.jpg', image)


