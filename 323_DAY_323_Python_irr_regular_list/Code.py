# **************** "iNNovationMerge DailyCodeHub" ****************
# Visit https://www.innovationmerge.com/
# Theme : Regular python3 codes

# Python program to convert Irregular List to Single List

import itertools

irr_list = [['a', 'a'], ['b', 'b'], ['c', 'c']]

single_list = list(itertools.chain.from_iterable(irr_list))  

print(single_list)

#Output : ['a', 'a', 'b', 'b', 'c', 'c']  






