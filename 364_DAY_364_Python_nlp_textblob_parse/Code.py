# **************** "iNNovationMerge DailyCodeHub" ****************
# Visit https://www.innovationmerge.com/

# Theme : Natural Language Processing using TextBlob in Python 

# NLP - Parsing the Text

from textblob import TextBlob

text = 'INNovationMerge is an online learning platform. \
        developed for the users who wants to learn and practice \
        technologies with the respective environments.'
blob = TextBlob(text)
print(blob.parse())

# Output:
# INNovationMerge/NN/B-NP/O is/VBZ/B-VP/O an/DT/O/O online/JJ/B-ADJP/O learning/VBG/B-VP/O platform/NN/B-NP/O ././O/O developed/VBN/B-VP/O for/IN/B-PP/B-PNP the/DT/B-NP/I-PNP users/NNS/I-NP/I-PNP who/WP/O/O wants/VBZ/B-VP/O to/TO/B-PP/O learn/VB/B-VP/O and/CC/O/O practice/NN/B-NP/O technologies/NNS/I-NP/O with/IN/B-PP/B-PNP the/DT/B-NP/I-PNP respective/JJ/I-NP/I-PNP environments/NNS/I-NP/I-PNP ././O/O





