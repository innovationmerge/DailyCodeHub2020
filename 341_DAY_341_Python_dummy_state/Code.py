# **************** "iNNovationMerge DailyCodeHub" ****************
# Visit https://www.innovationmerge.com/
# Theme : Dummy Data Generation in Python

# Python program generate dummy state 

from faker import Faker
fake = Faker("en_US")
for _ in range(10):
    print(fake.state())



""" 
# Output : 
    Kansas
    Vermont
    Texas
    Delaware
    New York
    Indiana
    Michigan
    Kansas
    Wisconsin
    Arkansas
"""

