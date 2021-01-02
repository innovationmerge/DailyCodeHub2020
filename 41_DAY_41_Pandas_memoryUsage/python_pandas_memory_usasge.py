# "iNNovationMerge DailyCodeHub"

# Python program to show how much memory is used by datafreame in bytes using pandas memory_usage function

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

# Check dataframe memory usage in bytes.
print(df.memory_usage())
"""
Output:
Index    128
A         40
B         40
dtype: int64
"""