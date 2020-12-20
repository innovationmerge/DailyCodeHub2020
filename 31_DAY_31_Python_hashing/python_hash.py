# "iNNovationMerge DailyCodeHub"

# Python program to encode iNNovationMerge using md5 hash 

import hashlib 

result = hashlib.md5(b'iNNovationMerge') 

# Print encoded string of iNNovationMerge in hexadecimal
print(result.hexdigest())                           
# Output 6b0ef1936309dedd9dc4fbb06c2f1c11

# Print  encoded string of iNNovationMerge in byte
print(result.digest())                              
# Output : b'k\x0e\xf1\x93c\t\xde\xdd\x9d\xc4\xfb\xb0l/\x1c\x11'
