# "iNNovationMerge DailyCodeHub"

# Theme : Debug week with Python

# Inspect Python code Execution using icecream instead of print

# Using print
def check_boolean(status):
    if status:
        print("True")
    else:
        print("False")
check_boolean(True)
#Output: True


#Using Icecream
#pip install icecream
from icecream import ic
def check_boolean(status):
    if status:
        ic()
    else:
        ic()
check_boolean(False)
#Output: ic| Python_inspect_icecream.py:
# 22 in check_boolean() at 06:01:54.725

