# **************** "iNNovationMerge DailyCodeHub" ****************
# Visit https://www.innovationmerge.com/
# Theme : Dummy Data Generation in Python

# Python program generate dummy sentence 

from faker import Faker
fake = Faker("en_US")
for _ in range(10):
    print(fake.sentence())



""" 
# Output : 
    American down agent contain beyond Republican method.
    Green ever job size.
    Language indeed bed machine free. 
    Experience speech fire five the.  
    Possible bit join attorney size.  
    Third history interview teach suffer total case.
    Media story pretty measure consumer less top financial.
    Tree history hit challenge space. 
    How few these everybody gas either data.
    Place feel become.
"""

