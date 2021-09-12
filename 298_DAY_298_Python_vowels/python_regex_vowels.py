# **************** "iNNovationMerge DailyCodeHub" ****************
# Visit https://www.innovationmerge.com/
# Theme : Week with Regular Expression

# Python program to find word starting with vowels

import re
string = "iNNovationMerge is an online learning platform"
print(re.findall(r'\b[aeiouAEIOU]\w+', string))

#Output : ['iNNovationMerge', 'is', 'an', 'online']









