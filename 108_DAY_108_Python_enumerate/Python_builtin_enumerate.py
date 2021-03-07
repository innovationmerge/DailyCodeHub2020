# "iNNovationMerge DailyCodeHub"

# Theme : Built in week with Python

# Python program to get index while looping

import json

for index, ele in enumerate(['1', '2', '3']):  
    print(f'index: {index}, element: {ele}')

#Output :
# index: 0, element: 1
# index: 1, element: 2
# index: 2, element: 3

result = list(enumerate(['1', '2', '3']))
print(result)

# Output : [(0, '1'), (1, '2'), (2, '3')]

