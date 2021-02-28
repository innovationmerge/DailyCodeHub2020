# "iNNovationMerge DailyCodeHub"

# Theme : WORD CLOUD week with Python

# Python program to Generate a square wordcloud based on frequencies

import os
from os import path
from wordcloud import WordCloud, STOPWORDS 
from collections import Counter
# Read the whole text.
text = open('iNNovationMergeReadme.txt').read().split(" ")
stopwords = set(STOPWORDS)
dictionary=Counter(text)
wordcloud = WordCloud(max_font_size=40, background_color ='white', stopwords = stopwords).generate_from_frequencies(dictionary)
# Display using PIL
image = wordcloud.to_image()
image.show()
