# **************** "iNNovationMerge DailyCodeHub" ****************
# Visit https://www.innovationmerge.com/
# Theme : Week with Regular Expression

# Python program to extract URL in string

import re
string = "iNNovationMerge website URL is https://www.innovationmerge.com"

x = re.findall('((http|https)://)(www.)?[a-zA-Z0-9@:%._\\+~#?&//=]{2,256}\\.[a-z]{2,6}\\b([-a-zA-Z0-9@:%._\\+~#?&//=]*)', string)
print(x)

#Output : [('https://', 'https', 'www.', '')]







