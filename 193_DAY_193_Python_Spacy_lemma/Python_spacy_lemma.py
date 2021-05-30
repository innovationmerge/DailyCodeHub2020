# "iNNovationMerge DailyCodeHub"

# Theme : Natural Language Processing using spaCy in Python

# NLP - Lemmatization using spaCy

# Installation - pip install spacy
# python -m spacy download en_core_web_sm

import spacy
import pandas as pd
nlp = spacy.load('en_core_web_sm')

text = ('iNNovationMerge is an online learning platform, \
        developed for the users who wants to learn and practice \
        technologies with the respective environments.')

nlp_doc = nlp(text)

result = [{"text": token.text, "Lemma": token.lemma_} 
         for token in nlp_doc]

# Create datafrane for result
df = pd.DataFrame(result)
print(df)

"""
               text            Lemma
0   iNNovationMerge  innovationmerge
1                is               be
2                an               an
3            online           online
4          learning         learning
5          platform         platform
6                 ,                ,
7
8         developed          develop
"""