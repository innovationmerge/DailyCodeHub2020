# "iNNovationMerge DailyCodeHub"

# Python program to transpose a dataframe

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

# Transpose Dataframe
df_transposed = df.T
print(df_transposed)
"""
Output:
    0   1   2   3   4
A   1   2   3   4   5
B  11  22  33  44  55
"""
