# **************** "iNNovationMerge DailyCodeHub" ****************
# Visit https://www.innovationmerge.com/

# Theme : Natural Language Processing using TextBlob in Python 

# NLP - Spell Check of Text

from textblob import Word

check = Word('innovationmerge')
print(check.spellcheck())


# Output:
# [('innovationmerge', 0.0)]





