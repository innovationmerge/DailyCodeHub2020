# "iNNovationMerge DailyCodeHub"

# Python program to calculate the percent change through the values in a series using pandas pct_change function

# pip install pandas

import pandas as pd
import numpy as np 

# Create Dataframe
df = pd.DataFrame({'A': [1, 2, 3, 4, 5],
                   'B': [11, 22, 33, 44, 55]})

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

# Calculating the percentage change through a column
print(df.pct_change())
"""
Output:
          A         B
0       NaN       NaN
1  1.000000  1.000000
2  0.500000  0.500000
3  0.333333  0.333333
4  0.250000  0.250000
"""