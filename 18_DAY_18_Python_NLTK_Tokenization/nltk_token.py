# iNNovationMerge

# Python program to Tokenize Words and Sentences with NLTK

# nltk - The Natural Language Toolkit (NLTK) is a Python package for natural language processing. 

# pip install nltk

from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize

text = "iNNovationMerge is an online learning platform. It is designed to answer every question that comes to the mind in the form of What?, Why?, How?, Where?."

print(word_tokenize(text))
# ['iNNovationMerge', 'is', 'an', 'online', 'learning', 'platform', '.', 'It', 'is', 'designed', 'to', 'answer', 'every', 'question', 'that', 'comes', 'to', 'the', 'mind', 'in', 'the', 'form', 'of', 'What', '?', ',', 'Why', '?', ',', 'How', '?', ',', 'Where', '?', '.']

print(sent_tokenize(text))
# ['iNNovationMerge is an online learning platform.', 'It is designed to answer every question that comes to the mind in the form of What?, Why?, How?, Where?.']

