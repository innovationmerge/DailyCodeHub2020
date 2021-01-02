# "iNNovationMerge DailyCodeHub"

# Python program to set required column as Index by using pandas set_index function

# pip install pandas

import pandas as pd
import numpy as np 

# Create Dataframe
df = pd.DataFrame({'A': '1 2 3 4 5'.split(),
                   'B': '11 22 33 44 55'.split()})

# Print Created Dataframe
print(df)
"""
Output:
   A   B
0  1  11
1  2  22
2  3  33
3  4  44
4  5  55
"""

# Set A as Index column by using set_index function
df.set_index('A', inplace=True)
print(df)
"""
Output:
A
1  11
2  22
3  33
4  44
5  55
"""
