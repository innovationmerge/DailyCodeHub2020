# **************** "iNNovationMerge DailyCodeHub" ****************
# Visit https://www.innovationmerge.com/
# Theme : Dummy Data Generation in Python

# Python program generate dummy names

from faker import Faker
fake = Faker("en_US")
for _ in range(10):
    print(fake.name())


""" 
# Output : 
    Robert Hernandez
    Roberto Griffith
    Richard Davis
    Phyllis Wilson
    Jacqueline Mitchell
    Joseph Mccann
    Matthew Quinn
    Brandon Moreno
    Linda Hoffman
    Sabrina Miller
"""

