# **************** "iNNovationMerge DailyCodeHub" ****************
# Visit https://www.innovationmerge.com/
# Theme : Dummy Data Generation in Python

# Python program generate dummy dates 

from faker import Faker
fake = Faker("en_US")
for _ in range(10):
    print(fake.date_between(start_date='-15y', end_date='today'))



""" 
# Output : 
    2019-12-31
    2020-01-01
    2020-05-12
    2020-06-27
    2020-02-05
    2018-10-06
    2010-10-11
    2021-03-18
    2013-02-15
    2008-08-10
"""

