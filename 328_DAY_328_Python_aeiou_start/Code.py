# **************** "iNNovationMerge DailyCodeHub" ****************
# Visit https://www.innovationmerge.com/
# Theme : Regular python3 codes

# Python program filter names which starts with aeiou

list_data = ['innovation', 'merge', 'learning', 'platform']
print(list(filter(lambda x: x[0].lower() in 'aeiou', list_data)))

""" 
#Output : ['innovation']
"""

