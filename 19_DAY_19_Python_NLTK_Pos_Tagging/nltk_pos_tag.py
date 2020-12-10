# iNNovationMerge

# Python program to Generate POS(Parts of Speech) Tag for given text using NLTK Toolkit

# nltk - The Natural Language Toolkit (NLTK) is a Python package for natural language processing. 

# pip install nltk

import nltk
from nltk.tokenize import word_tokenize

text = "iNNovationMerge is an online learning platform. It is designed to answer every question that comes to the mind in the form of What?, Why?, How?, Where?."

text_tokens = word_tokenize(text)
print(nltk.pos_tag(text_tokens))
# [('iNNovationMerge', 'NN'), ('is', 'VBZ'), ('an', 'DT'), ('online', 'JJ'), ('learning', 'NN'), ('platform', 'NN'), ('.', '.'), ('It', 'PRP'), ('is', 'VBZ'), ('designed', 'VBN'), ('to', 'TO'), ('answer', 'VB'), ('every', 'DT'), ('question', 'NN'), ('that', 'WDT'), ('comes', 'VBZ'), ('to', 'TO'), ('the', 'DT'), ('mind', 'NN'), ('in', 'IN'), ('the', 'DT'), ('form', 'NN'), ('of', 'IN'), ('What', 'WP'), ('?', '.'), (',', ','), ('Why', 'WRB'), ('?', '.'), (',', ','), ('How', 'WRB'), ('?', '.'), (',', ','), ('Where', 'WRB'), ('?', '.'), ('.', '.')]