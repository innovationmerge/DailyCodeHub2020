# **************** "iNNovationMerge DailyCodeHub" ****************
# Visit https://www.innovationmerge.com/
# Theme : Dummy Data Generation in Python

# Python program generate dummy boolean 

from faker import Faker
fake = Faker("en_US")
for _ in range(10):
    print(fake.boolean())



""" 
# Output : 
    True
    False
    False
    True
    False
    False
    True
    False
    True
    True
"""

