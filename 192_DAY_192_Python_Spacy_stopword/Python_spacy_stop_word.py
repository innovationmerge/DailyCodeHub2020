# "iNNovationMerge DailyCodeHub"

# Theme : Natural Language Processing using spaCy in Python

# NLP - Remove stopwords in text using spaCy

# Installation - pip install spacy
# python -m spacy download en_core_web_sm

import spacy
nlp = spacy.load('en_core_web_sm')

stopwords_list = spacy.lang.en.stop_words.STOP_WORDS

text = ('iNNovationMerge is an online learning platform, \
        developed for the users who wants to learn and practice \
        technologies with the respective environments.')

nlp_doc = nlp(text)

print ([token.text for token in nlp_doc if token.text not in stopwords_list])

# Output : ['iNNovationMerge', 'online', 'learning', 'platform', ',', '        ', 'developed', 'users', 'wants', 'learn', 'practice', '        ', 'technologies', 'respective', 'environments', '.']