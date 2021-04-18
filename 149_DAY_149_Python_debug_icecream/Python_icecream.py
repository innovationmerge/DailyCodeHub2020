# "iNNovationMerge DailyCodeHub"

# Theme : Debug week with Python

# Debugging Python code using icecream instead of print

str1 = "iNNovationMerge"
str2 = "DailyCodeHub"

# Using print
print(str1)                 # iNNovationMerge
print(str2)                 # DailyCodeHub

#Using Icecream
#pip install icecream
from icecream import ic 
ic(str1)                 # ic| str1: 'iNNovationMerge'
ic(str2)                 # ic| str2: 'DailyCodeHub'

