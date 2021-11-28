# **************** "iNNovationMerge DailyCodeHub" ****************
# Visit https://www.innovationmerge.com/
# Theme : Dummy Data Generation in Python

# Python program generate dummy ssn 

from faker import Faker
fake = Faker("en_US")
for _ in range(10):
    print(fake.ssn())



""" 
# Output : 
    056-27-0311
    812-10-9801
    393-55-7113
    423-04-2170
    803-06-9931
    558-15-7487
    040-03-9116
    835-38-7805
    429-28-0813
    166-62-3703
"""

