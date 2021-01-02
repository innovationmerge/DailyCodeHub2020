# "iNNovationMerge DailyCodeHub"

# Python program to convert string to int and add a number using pandas apply function

# pip install pandas

import pandas as pd

# Create Dataframe
df = pd.DataFrame({'string_number': ['111', '222', '333']})
print(df)
"""
  string_number
0           111
1           222
2           333
"""

# apply a function to convert string(n) to int and add 1 to it.
df = df.string_number.apply(lambda n: int(n)+1)
print(df)
"""
0    112
1    223
2    334
Name: string_number, dtype: int64
"""

