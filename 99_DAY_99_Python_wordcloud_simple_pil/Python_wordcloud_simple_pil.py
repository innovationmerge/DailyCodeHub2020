# "iNNovationMerge DailyCodeHub"

# Theme : WORD CLOUD week with Linux

# Python program to Generate a square wordcloud and display using PIL 

import os
from os import path
from wordcloud import WordCloud, STOPWORDS 

# Read the whole text.
text = open('iNNovationMergeReadme.txt').read()
stopwords = set(STOPWORDS)
wordcloud = WordCloud(max_font_size=40, background_color ='white', stopwords = stopwords).generate(text)
# Display using PIL
image = wordcloud.to_image()
image.show()
