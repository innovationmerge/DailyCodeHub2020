# **************** "iNNovationMerge DailyCodeHub" ****************
# Visit https://www.innovationmerge.com/
# Theme : Week with image preprocessing using OpenCV

# Python program to apply dilation to an image

import cv2
import os
import numpy as np
image = cv2.imread('test.jpg', cv2.IMREAD_GRAYSCALE)
kernel = np.ones((3,3),np.uint8)
image = cv2.dilate(image, kernel, iterations = 1)
cv2.imwrite('test_output.jpg', image)


