# **************** "iNNovationMerge DailyCodeHub" ****************
# Visit https://www.innovationmerge.com/

# Theme : Natural Language Processing using TextBlob in Python 

# NLP - Part-of-speech Tagging of Text

from textblob import TextBlob

text = 'iNNovationMerge is an online learning platform, \
        developed for the users who wants to learn and practice \
        technologies with the respective environments.'
blob = TextBlob(text)
print(blob.tags)

# Output:
# [('iNNovationMerge', 'NN'), ('is', 'VBZ'), ('an', 'DT'), ('online', 'JJ'), ('learning', 'NN'), ('platform', 'NN'), ('developed', 'VBN'), ('for', 'IN'), ('the', 'DT'), ('users', 'NNS'), ('who', 'WP'), ('wants', 'VBZ'), ('to', 'TO'), ('learn', 'VB'), ('and', 'CC'), ('practice', 'NN'), ('technologies', 'NNS'), ('with', 'IN'), ('the', 'DT'), ('respective', 'JJ'), ('environments', 'NNS')]





