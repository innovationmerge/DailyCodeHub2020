# **************** "iNNovationMerge DailyCodeHub" ****************
# Visit https://www.innovationmerge.com/
# Theme : Week with Regular Expression

# Python program to convert date format from YYY-MM-DD to DD/MM/YYYY

import re
string = "2021-05-27"
print(re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', 
             '\\3/\\2/\\1', string))

#Output : 27/05/2021








