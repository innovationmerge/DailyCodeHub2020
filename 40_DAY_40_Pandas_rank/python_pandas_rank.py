# "iNNovationMerge DailyCodeHub"

# Python program to assigns a rank to the values using pandas rank function

# pip install pandas

import pandas as pd
import numpy as np 

# Create Dataframe
df = pd.DataFrame({'A': [1, 2, 3, 4, 5],
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

# Rank Column A 
df['rank'] = df['A'].rank(method='first', ascending=False).astype('int')
print(df)
"""
Output:
   A   B  rank
0  1  11     5
1  2  22     4
2  3  33     3
3  4  44     2
4  5  55     1
"""
