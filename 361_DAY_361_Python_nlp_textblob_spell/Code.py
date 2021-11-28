# **************** "iNNovationMerge DailyCodeHub" ****************
# Visit https://www.innovationmerge.com/

# Theme : Natural Language Processing using TextBlob in Python 

# NLP - Spelling Correction of Text

from textblob import TextBlob

text = 'INNovationMerg is an onlin learning platform.'
blob = TextBlob(text)
print(blob.correct())

# Output:
# INNovationMerg is an online learning platform.





