# **************** "iNNovationMerge DailyCodeHub" ****************
# Visit https://www.innovationmerge.com/
# Theme : Week with Regular Expression

# Python program to extract Date in string

import re
string = "iNNovationMerge new courses are available from 29/08/2021"

x = re.findall('[0-9]{1,2}\/[0-9]{1,2}\/[0-9]{4}', string)
print(x)

#Output : ['29/08/2021']







