# **************** "iNNovationMerge DailyCodeHub" ****************
# Visit https://www.innovationmerge.com/
# Theme : Dummy Data Generation in Python

# Python program generate dummy latitude and longitude

from faker import Faker
fake = Faker("en_US")
for _ in range(10):
    print(fake.latitude(), fake.longitude())


""" 
# Output : 
    34.934802 31.380990
    75.7982075 89.837247
    2.658317 -107.757149
    71.6035545 -97.795419
    -47.979294 -64.769139
    73.2208715 138.577491
    65.385099 161.275268
    34.3916815 171.350860
    49.102953 54.729642
    -17.187314 7.723509
"""

