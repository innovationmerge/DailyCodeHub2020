# "iNNovationMerge DailyCodeHub"

# Theme : Debug week with Python

# Debug Python code with logging using icecream

#pip install icecream

import logging
from icecream import ic

def warn(s):
    logging.warning(s)

ic.configureOutput(outputFunction=warn)
def check_boolean(status):
    if status:
        ic("True")
    else:
        ic("False")
check_boolean(True)
#Output: WARNING:root:ic| 'True'

