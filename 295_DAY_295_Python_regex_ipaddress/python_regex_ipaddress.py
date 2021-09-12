# **************** "iNNovationMerge DailyCodeHub" ****************
# Visit https://www.innovationmerge.com/
# Theme : Week with Regular Expression

# Python program to extract IP address in the string

import re
string = "192.168.1.1, 192.168.1.2, 0000.1680.1.2"
pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
new_string = pattern.findall(string)

print(new_string)

#Output : ['192.168.1.1', '192.168.1.2'] 








