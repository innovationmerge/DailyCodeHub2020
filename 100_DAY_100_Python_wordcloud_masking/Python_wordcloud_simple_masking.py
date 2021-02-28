# "iNNovationMerge DailyCodeHub"

# Theme : WORD CLOUD week with Linux

# Python program to Generate a wordcloud with masking
import os
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_gradient_magnitude
from wordcloud import WordCloud, ImageColorGenerator

# load iNNovationMerge DailyCodeHub Readme
text = open('iNNovationMergeReadme.txt', encoding="utf-8").read()
# load masking image
parrot_color = np.array(Image.open("parrot-by-jose-mari-gimenez2.jpg"))
# subsample by factor of 3
parrot_color = parrot_color[::3, ::3]
# create mask  white is "masked out"
parrot_mask = parrot_color.copy()
parrot_mask[parrot_mask.sum(axis=2) == 0] = 255
edges = np.mean([gaussian_gradient_magnitude(parrot_color[:, :, i] / 255., 2) for i in range(3)], axis=0)
parrot_mask[edges > .08] = 255
# Create wordcloud.
wc = WordCloud(max_words=2000, mask=parrot_mask, max_font_size=120, random_state=20, 
relative_scaling=0, background_color ='white', collocations=False)

# Generate word cloud
plt.figure(figsize=(10, 10))
wc.generate(text)
plt.imshow(wc)
plt.show()

# Display original image
plt.figure(figsize=(10, 10))
plt.title("Original Image")
plt.imshow(parrot_color)

# Display Edge map
plt.figure(figsize=(10, 10))
plt.title("Edge map")
plt.imshow(edges)
plt.show()

# create coloring from image
image_colors = ImageColorGenerator(parrot_color)
wc.recolor(color_func=image_colors)
plt.figure(figsize=(10, 10))
plt.imshow(wc, interpolation="bilinear")
wc.to_file("parrot_new.png")

