# **************** "iNNovationMerge DailyCodeHub" ****************
# Visit https://www.innovationmerge.com/
# Theme : Week with image preprocessing using OpenCV

# Python program to apply blur to an image

import cv2
import os
import numpy as np
image = cv2.imread('test.jpg', cv2.IMREAD_GRAYSCALE)
image = cv2.blur(image,(5,5))
cv2.imwrite('test_output.jpg', image)


