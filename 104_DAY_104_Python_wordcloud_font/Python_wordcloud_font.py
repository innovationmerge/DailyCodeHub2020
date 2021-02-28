# "iNNovationMerge DailyCodeHub"

# Theme : WORD CLOUD week with Python

# Python program to Generate a square wordcloud with custom font

import os
from os import path
from wordcloud import WordCloud, STOPWORDS 

d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()
# Read the whole text.
text = open('iNNovationMergeReadme.txt').read()
stopwords = set(STOPWORDS)

font_path = path.join(d, 'fonts', 'Symbola', 'Symbola.ttf')
wordcloud = WordCloud(font_path=font_path, background_color ='white', stopwords = stopwords).generate(text)
# Display using PIL
image = wordcloud.to_image()
image.show()

