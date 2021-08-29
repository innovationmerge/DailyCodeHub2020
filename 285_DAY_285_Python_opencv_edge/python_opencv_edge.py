# **************** "iNNovationMerge DailyCodeHub" ****************
# Visit https://www.innovationmerge.com/
# Theme : Week with image preprocessing using OpenCV

# Python program to apply canny edge detection to an image

import cv2
import os
import numpy as np
image = cv2.imread('test.jpg', cv2.IMREAD_GRAYSCALE)
image = cv2.Canny(image, 100, 200)
cv2.imwrite('test_output.jpg', image)


