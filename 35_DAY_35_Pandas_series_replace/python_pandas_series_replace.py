# "iNNovationMerge DailyCodeHub"

# Python program to Remove the dash(-) from all element in the Series

# pip install pandas

import pandas as pd


S=pd.Series(['A-1', 'A-2', 'A-3', 'A-4', 'A-5'])
print(S)
"""
0    A-1
1    A-2
2    A-3
3    A-4
4    A-5
dtype: object
"""
# Remove the dash(-) from all element in the Series
S.replace('(-)','',regex=True, inplace = True)
print(S)
"""
0    A1
1    A2
2    A3
3    A4
4    A5
dtype: object
"""