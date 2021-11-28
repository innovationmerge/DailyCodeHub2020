# **************** "iNNovationMerge DailyCodeHub" ****************
# Visit https://www.innovationmerge.com/
# Theme : Regular python3 codes

# Python program to get password from cmd

import getpass
passwd = getpass.getpass('Password:')

# Check the password
if passwd == "innovationmerge":
    print("You are authenticated")
else:
    print("You are not authenticated")

""" 
#Output :
  Password:
  You are authenticated
"""

