# "iNNovationMerge DailyCodeHub"

# Python program to convert date strings into the datetime objects.

# pip install pandas

import pandas as pd

# Create Dataframe
df = pd.DataFrame({'date_column': ['11/02/2020', '12/02/2020', '13/02/2020']})
print(df)
"""
  date_column
0  11/02/2020
1  12/02/2020
2  13/02/2020
"""
print(df.dtypes)
# date_column    object

# Convert to  datetime objects.
df = pd.to_datetime(df.date_column, format='%d/%m/%Y')
print(df)
"""
0   2020-02-11
1   2020-02-12
2   2020-02-13
Name: date_column, dtype: datetime64[ns]
"""
print(df.dtypes)
# datetime64[ns]

