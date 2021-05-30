# "iNNovationMerge DailyCodeHub"

# Theme : Natural Language Processing using spaCy in Python

# NLP - Unique words generation using spaCy

# Installation - pip install spacy
# python -m spacy download en_core_web_sm

import spacy
import pandas as pd
from collections import Counter
nlp = spacy.load('en_core_web_sm')

text = ('iNNovationMerge is an online learning platform, \
        developed for the users who wants to learn and practice \
        technologies with the respective environments.')

nlp_doc = nlp(text)

words = [token.text for token in nlp_doc]
word_freq = Counter(words)
unique_words = [word for (word, freq) in word_freq.items() if freq == 1]
print (unique_words)

"""
['iNNovationMerge', 'is', 'an', 'online', 'learning', 'platform', ',', 'developed', 'for', 'users', 'who', 'wants', 'to', 'learn', 'and', 'practice', 'technologies', 'with', 'respective', 'environments', '.']
"""