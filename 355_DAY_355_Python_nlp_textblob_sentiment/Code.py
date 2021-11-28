# **************** "iNNovationMerge DailyCodeHub" ****************
# Visit https://www.innovationmerge.com/

# Theme : Natural Language Processing using TextBlob in Python 

# NLP - Sentiment Analysis of Text

from textblob import TextBlob

text = 'INNovationMerge is an online learning platform, \
        developed for the users who wants to learn and practice \
        technologies with the respective environments.'
blob = TextBlob(text)
print(blob.sentiment)

# Output:
# Sentiment(polarity=0.10000000000000002, subjectivity=0.16666666666666666)





