# **************** "iNNovationMerge DailyCodeHub" ****************
# Visit https://www.innovationmerge.com/
# Theme : Dummy Data Generation in Python

# Python program generate dummy URL 

from faker import Faker
fake = Faker("en_US")
for _ in range(10):
    print(fake.url())


""" 
# Output : 
    https://www.bishop-rich.info/     
    https://johnson.info/
    https://www.aguilar.net/
    http://dixon.com/
    https://adams.biz/
    https://chandler.com/
    http://www.leonard-baldwin.com/   
    http://glass.com/
    http://www.robinson.com/
    https://www.glass-stout.biz/
"""

