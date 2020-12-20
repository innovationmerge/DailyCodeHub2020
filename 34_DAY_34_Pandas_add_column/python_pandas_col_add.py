# "iNNovationMerge DailyCodeHub"

# Python program to Add a new column to an existing Pandas DataFrame

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

# Adding a new column to an existing DataFram
df['C']=pd.Series([111,222,333,444,555])

print(df)
"""
   A   B    C
0  1  11  111
1  2  22  222
2  3  33  333
3  4  44  444
4  5  55  555
"""
