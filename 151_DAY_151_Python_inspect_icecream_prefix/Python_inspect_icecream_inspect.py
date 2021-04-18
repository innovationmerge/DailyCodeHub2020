# "iNNovationMerge DailyCodeHub"

# Theme : Debug week with Python

# Debug Python code with custom prefix using icecream instead of print

from datetime import datetime
def get_datetime():
    return str(datetime.now()) + " : "


# Using print
def check_boolean(status):
    if status:
        print(get_datetime() +  " True")
    else:
        print(get_datetime() +  " False")
check_boolean(True)
#Output: 2021-04-11 11:42:54.046729 :  True


#Using Icecream
#pip install icecream
from icecream import ic
ic.configureOutput(prefix=get_datetime)
def check_boolean(status):
    if status:
        ic("True")
    else:
        ic("False")
check_boolean(False)
#Output: 2021-04-11 11:42:54.176384 : 'False'

