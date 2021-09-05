# **************** "iNNovationMerge DailyCodeHub" ****************
# Visit https://www.innovationmerge.com/
# Theme : Week with Regular Expression

# Python program to match the start of the string

import re
string = "iNNovationMerge is an online learning platform"
x = re.findall("^iNNovationMerge", string)
print(x)

#Output : ['iNNovationMerge']


