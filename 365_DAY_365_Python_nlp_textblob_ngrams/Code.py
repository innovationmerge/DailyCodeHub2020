# **************** "iNNovationMerge DailyCodeHub" ****************
# Visit https://www.innovationmerge.com/

# Theme : Natural Language Processing using TextBlob in Python 

# NLP - n successive words of Text

from textblob import TextBlob

text = 'INNovationMerge is an online learning platform. \
        developed for the users who wants to learn and practice \
        technologies with the respective environments.'
blob = TextBlob(text)
print(blob.ngrams(n=2))

# Output:
# [WordList(['INNovationMerge', 'is']), WordList(['is', 'an']), WordList(['an', 'online']), WordList(['online', 'learning']), WordList(['learning', 'platform']), WordList(['platform', 'developed']), WordList(['developed', 'for']), WordList(['for', 'the']), WordList(['the', 'users']), WordList(['users', 'who']), WordList(['who', 'wants']), WordList(['wants', 'to']), WordList(['to', 'learn']), WordList(['learn', 'and']), WordList(['and', 'practice']), WordList(['practice', 'technologies']), WordList(['technologies', 'with']), WordList(['with', 'the']), WordList(['the', 'respective']), WordList(['respective', 'environments'])]






