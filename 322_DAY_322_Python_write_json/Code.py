# **************** "iNNovationMerge DailyCodeHub" ****************
# Visit https://www.innovationmerge.com/
# Theme : Regular python3 codes

# Python program to write JSON file

import json

data = {'SL1': 1, 'SL2': 2}
with open('data.json', 'w') as f:
  json.dump(data, f, ensure_ascii=False)

#Output : {'SL1': 1, 'SL2': 2}







