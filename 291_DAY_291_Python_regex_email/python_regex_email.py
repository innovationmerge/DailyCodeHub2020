# **************** "iNNovationMerge DailyCodeHub" ****************
# Visit https://www.innovationmerge.com/
# Theme : Week with Regular Expression

# Python program to extract Email ID in string

import re
string = "iNNovationMerge Email ID is innovationmerge@gmail.com"
x = re.findall('[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$', string)
print(x)

#Output : ['innovationmerge@gmail.com']





