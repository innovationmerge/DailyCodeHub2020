# **************** "iNNovationMerge DailyCodeHub" ****************
# Visit https://www.innovationmerge.com/
# Theme : Dummy Data Generation in Python

# Python program generate dummy month 

from faker import Faker
fake = Faker("en_US")
for _ in range(10):
    print(fake.month())



""" 
# Output : 
    05
    06
    02
    06
    07
    11
    11
    06
    03
    06
"""

