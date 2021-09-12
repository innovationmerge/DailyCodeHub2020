# **************** "iNNovationMerge DailyCodeHub" ****************
# Visit https://www.innovationmerge.com/
# Theme : Week with Regular Expression

# Python program to extract replace whitespace characters in string

import re
string = "iNNovationMerge new courses are available \nfrom 29/08/2021"
pattern = '\s+'
replace = ""
new_string = re.subn(pattern, replace, string) 
print(new_string)

#Output : ('iNNovationMergenewcoursesareavailablefrom29/08/2021', 6) 








