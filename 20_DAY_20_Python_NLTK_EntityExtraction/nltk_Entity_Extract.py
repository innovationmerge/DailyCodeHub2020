# iNNovationMerge

# Python program to Extract Entities for given text using NLTK Toolkit

# nltk - The Natural Language Toolkit (NLTK) is a Python package for natural language processing. 

# pip install nltk

import nltk
from nltk.tokenize import word_tokenize

text = "iNNovationMerge is an online learning platform from India. It is designed to answer every question that comes to your mind in the form of What?, Why?, How?, Where?."

text_tokens = word_tokenize(text)
tagged = nltk.pos_tag(text_tokens)
namedEnt = nltk.ne_chunk(tagged, binary=False)

print(namedEnt)

#  (ORGANIZATION iNNovationMerge/NN), (GPE India/NNP)