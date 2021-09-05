# **************** "iNNovationMerge DailyCodeHub" ****************
# Visit https://www.innovationmerge.com/
# Theme : Week with Regular Expression

# Python program to match the end of the string

import re
string = "iNNovationMerge! is an online learning platform"
x = re.findall("platform$", string)
print(x)

#Output : ['platform']



