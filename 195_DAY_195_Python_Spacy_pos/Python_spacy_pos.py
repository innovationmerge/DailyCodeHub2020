# "iNNovationMerge DailyCodeHub"

# Theme : Natural Language Processing using spaCy in Python

# NLP - Part of Speech Tagging using spaCy

# Installation - pip install spacy
# python -m spacy download en_core_web_sm

import spacy
import pandas as pd
nlp = spacy.load('en_core_web_sm')

text = ('iNNovationMerge is an online learning platform, \
        developed for the users who wants to learn and practice \
        technologies with the respective environments.')

nlp_doc = nlp(text)

result = [{"Text": token.text, "Tag": token.tag_, "POS" : token.pos_, 
        "Explanation" : spacy.explain(token.tag_)} for token in nlp_doc]

# Create datafrane for result
df = pd.DataFrame(result)
print(df)

"""
               Text  Tag    POS                                Explanation
0   iNNovationMerge   NN   NOUN                     noun, singular or mass
1                is  VBZ    AUX          verb, 3rd person singular present
2                an   DT    DET                                 determiner
3            online   JJ    ADJ                                  adjective
4          learning   NN   NOUN                     noun, singular or mass
5          platform   NN   NOUN                     noun, singular or mass
6                 ,    ,  PUNCT                    punctuation mark, comma
7                    _SP  SPACE                                       None
8         developed  VBD   VERB                           verb, past tense
9               for   IN    ADP  conjunction, subordinating or preposition
10              the   DT    DET                                 determiner
11            users  NNS   NOUN                               noun, plural
12              who   WP   PRON                       wh-pronoun, personal
13            wants  VBZ   VERB          verb, 3rd person singular present
14               to   TO   PART                           infinitival "to"
15            learn   VB   VERB                            verb, base form
"""