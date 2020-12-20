# "iNNovationMerge DailyCodeHub"
# Python program to select rows from a DataFrame based on column values

# pip install pandas

import pandas as pd
import numpy as np

# Create Dataframe
df = pd.DataFrame({'A': '1 2 3 4 5'.split(),
                   'B': '11 22 33 44 55'.split()})

# Print Created Datafrane
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

# Print dataframe where Column A has value 1
print(df.loc[df['A'] == "1"])
"""
Output:
   A   B
0  1  11
"""

# Print dataframe where Column A has value 2
print(df.loc[df['A'] == "3"])
"""
Output:
   A   B
2  3  33
"""