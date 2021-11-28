# **************** "iNNovationMerge DailyCodeHub" ****************
# Visit https://www.innovationmerge.com/

# Theme : Natural Language Processing using TextBlob in Python 

# NLP - Noun Phrase Extraction of Text

from textblob import TextBlob

text = 'INNovationMerge is an online learning platform, \
        developed for the users who wants to learn and practice \
        technologies with the respective environments.'
blob = TextBlob(text)
print(blob.noun_phrases)

# Output:
# ['innovationmerge', 'online learning platform', 'practice, technologies', 'respective environments']





