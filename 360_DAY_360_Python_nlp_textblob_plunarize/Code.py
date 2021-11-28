# **************** "iNNovationMerge DailyCodeHub" ****************
# Visit https://www.innovationmerge.com/

# Theme : Natural Language Processing using TextBlob in Python 

# NLP - Pluralize a Word

from textblob import TextBlob

text = 'INNovationMerge is an online learning platform. \
        developed for the users who wants to learn and practice \
        technologies with the respective environments.'
blob = TextBlob(text)
print(blob.words[5].pluralize())

# Output:
# platforms





