# "iNNovationMerge DailyCodeHub"

# Python program to create jpg/png image from base64 string

# pip install pillow

import base64
import io
from PIL import Image

base_mage = open("iNNovationMerge_encoded.txt", "r")

image_decode = base64.b64decode(str(base_mage.read()))
image = Image.open(io.BytesIO(image_decode))
image.save("base64image.png")
image.show()