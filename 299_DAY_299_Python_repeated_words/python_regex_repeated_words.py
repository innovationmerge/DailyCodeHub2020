# **************** "iNNovationMerge DailyCodeHub" ****************
# Visit https://www.innovationmerge.com/
# Theme : Week with Regular Expression

# Python program to remove repeated words in string

import re
Pattern = r"\b(\w+)(?:\W\1\b)+"
string = "iNNovationMerge iNNovationMerge is an online learning platform"
print(re.sub(Pattern, r"\1", string, flags=re.IGNORECASE))

#Output : iNNovationMerge is an online learning platform

