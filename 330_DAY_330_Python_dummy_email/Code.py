# **************** "iNNovationMerge DailyCodeHub" ****************
# Visit https://www.innovationmerge.com/
# Theme : Dummy Data Generation in Python

# Python program generate dummy emails

from faker import Faker
fake = Faker("en_US")
for _ in range(10):
    print(fake.email())


""" 
# Output : 
    marypage@example.net
    ywright@example.com
    oknight@example.org
    phillipsnathan@example.net        
    stephanie80@example.com
    gallowaykenneth@example.com       
    ryan05@example.net
    jlynch@example.net
    zward@example.org
    aaron90@example.org
"""

