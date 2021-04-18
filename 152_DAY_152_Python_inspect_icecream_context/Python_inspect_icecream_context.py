# "iNNovationMerge DailyCodeHub"

# Theme : Debug week with Python

# Debug Python code with more context using icecream instead of print

from datetime import datetime
def get_datetime():
    return str(datetime.now()) + " : "


# Using print
def check_boolean(status):
    if status:
        print(get_datetime() + "True")
    else:
        print(get_datetime() + "False")
check_boolean(True)
#Output: 2021-04-11 11:50:53.758694 : True

from datetime import datetime
def get_datetime():
    return str(datetime.now()) + " : "

#Using Icecream
#pip install icecream
from icecream import ic
ic.configureOutput(includeContext=True)
def check_boolean(status):
    if status:
        ic("True")
    else:
        ic("False")
check_boolean(False)
#Output: ic| Python_inspect_icecream_context.py:30 
# in check_boolean()- 'False'

