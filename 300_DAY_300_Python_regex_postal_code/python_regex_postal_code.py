# **************** "iNNovationMerge DailyCodeHub" ****************
# Visit https://www.innovationmerge.com/
# Theme : Week with Regular Expression

# Python program to extract postal code in the string

import re
string = "560064"
pattern = re.compile(r'\b(\d[\- ]*){6}\b(?<! )')
new_string = pattern.match(string)[0]

print(new_string)

#Output : 560064








