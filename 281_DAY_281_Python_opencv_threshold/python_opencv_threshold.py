# **************** "iNNovationMerge DailyCodeHub" ****************
# Visit https://www.innovationmerge.com/
# Theme : Week with image preprocessing using OpenCV

# Python program for applying threshold to an image

import cv2
import os 
image = cv2.imread('test.jpg', cv2.IMREAD_GRAYSCALE)
image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
cv2.imwrite('test_output.jpg', image)


