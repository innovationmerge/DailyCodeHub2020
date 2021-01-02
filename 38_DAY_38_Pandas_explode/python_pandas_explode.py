# "iNNovationMerge DailyCodeHub"

# Python program to flatten JSON array under the same key using pandas explode function

# pip install pandas

import pandas as pd
json_data = [
  {
    'score': '99%',
    'names': [ 'Akshay', 'Ajay' ]
  },
  {
    'score': '95%',
    'names': [ 'kiran', 'joy']
  }
]
# Create Dataframe
df = pd.DataFrame(json_data)
print(df)
"""
  score           names
0   99%  [Akshay, Ajay]
1   95%    [kiran, joy]
"""

df = df.explode('names')
print(df)
"""
  score   names
0   99%  Akshay
0   99%    Ajay
1   95%   kiran
1   95%     joy
"""

