# "iNNovationMerge DailyCodeHub"

# Theme : Natural Language Processing using spaCy in Python

# NLP - Identify Text attributes using spaCy

# Installation - pip install spacy
# python -m spacy download en_core_web_sm

import spacy
import pandas as pd
nlp = spacy.load('en_core_web_sm')

text = ('iNNovationMerge is an online learning platform, \
        developed for the users who wants to learn and practice \
        technologies with the respective environments.')

nlp_doc = nlp(text)

result = [{"text": token.text, "index": token.idx, 
        "text_with_ws": token.text_with_ws, "is_alpha" : token.is_alpha, "is_punct" : token.is_punct, 
        "is_space" : token.is_space, "shape_" : token.shape_, "is_stop" : token.is_stop} 
         for token in nlp_doc]

# Create datafrane for result
df = pd.DataFrame(result)
print(df)

"""
               text  index      text_with_ws  is_alpha  is_punct  is_space        shape_  is_stop
0   iNNovationMerge      0  iNNovationMerge       True     False     False  xXXxxxxXxxxx    False
1                is     16               is       True     False     False            xx     True
2                an     19               an       True     False     False            xx     True
3            online     22           online       True     False     False          xxxx    False
4          learning     29         learning       True     False     False          xxxx    False
5          platform     38          platform      True     False     False          xxxx    False
6                 ,     46                ,      False      True     False             ,    False
7                       48                       False     False      True                  False
8         developed     56        developed       True     False     False          xxxx    False
9               for     66              for       True     False     False           xxx     True
10              the     70              the       True     False     False           xxx     True
11            users     74            users       True     False     False          xxxx    False
12              who     80              who       True     False     False           xxx     True
13            wants     84            wants       True     False     False          xxxx    False
14               to     90               to       True     False     False            xx     True
15            learn     93            learn       True     False     False          xxxx    False
16              and     99              and       True     False     False           xxx     True
17         practice    103         practice       True     False     False          xxxx    False
18                     112                       False     False      True                  False
19     technologies    120     technologies       True     False     False          xxxx    False
20             with    133             with       True     False     False          xxxx     True
21              the    138              the       True     False     False           xxx     True
22       respective    142       respective       True     False     False          xxxx    False
23     environments    153      environments      True     False     False          xxxx    False
24                .    165                 .     False      True     False             .    False
"""