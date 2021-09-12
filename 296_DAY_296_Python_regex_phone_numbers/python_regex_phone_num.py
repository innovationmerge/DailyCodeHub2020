# **************** "iNNovationMerge DailyCodeHub" ****************
# Visit https://www.innovationmerge.com/
# Theme : Week with Regular Expression

# Python program to extract phone numbers in the string

import re
string = "080-6565869"
print(re.findall(r'^(\d{3}-\d{7})$',string))

#Output : ['080-6565869']








