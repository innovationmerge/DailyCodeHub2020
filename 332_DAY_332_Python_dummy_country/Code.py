# **************** "iNNovationMerge DailyCodeHub" ****************
# Visit https://www.innovationmerge.com/
# Theme : Dummy Data Generation in Python

# Python program generate dummy country

from faker import Faker
fake = Faker("en_US")
for _ in range(10):
    print(fake.country())


""" 
# Output : 
    Timor-Leste
    Bahrain
    Switzerland
    Germany
    Bahrain
    Panama
    Qatar
    Mali
    Libyan Arab Jamahiriya
    Kazakhstan
"""

