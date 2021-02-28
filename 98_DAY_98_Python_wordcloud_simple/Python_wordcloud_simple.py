# "iNNovationMerge DailyCodeHub"

# Theme : WORD CLOUD week with Linux

# Python program to Generate a square wordcloud and plot using matplotlib

# pip install wordcloud
import os
from os import path
from wordcloud import WordCloud, STOPWORDS 

# Read the whole text
text = open('iNNovationMergeReadme.txt').read()
stopwords = set(STOPWORDS)
import matplotlib.pyplot as plt
wordcloud = WordCloud(max_font_size=40, background_color ='black', stopwords = stopwords).generate(text)
# Display the generated image using matplotlib
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()

