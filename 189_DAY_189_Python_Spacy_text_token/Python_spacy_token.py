# "iNNovationMerge DailyCodeHub"

# Theme : Natural Language Processing using spaCy in Python

# NLP - Text Tokenization using spaCy

# Installation - pip install spacy
# python -m spacy download en_core_web_sm

import spacy
nlp = spacy.load('en_core_web_sm')

text = ('iNNovationMerge is an online learning platform, \
        developed for the users who wants to learn and practice \
        technologies with the respective environments.')

nlp_doc = nlp(text)

print ([token.text for token in nlp_doc])

# Output : ['iNNovationMerge', 'is', 'an', 'online', 'learning', 'platform', ',', 'developed', 'for', 'the', 'users', 'who', 'wants', 'to', 'learn', 'and', 'practice', 'technologies', 'with', 'the', 'respective', 'environments', '.']