# **************** "iNNovationMerge DailyCodeHub" ****************
# Visit https://www.innovationmerge.com/
# Theme : Regular python3 codes

# Python program to Read and write using pickle

import pickle

test_list = ["iNNovation", "Merge"]

file_handler = open('pickle_file', 'wb')
pickle.dump(test_list, file_handler)
file_handler.close()

file_handler = open('pickle_file', 'rb')
test_list = pickle.load(file_handler)
for list_data in test_list:
  print('The data from pickle_file : ', list_data)
file_handler.close()

""" 
#Output :
    The data from pickle_file :  iNNovation
    The data from pickle_file :  Merge
"""

