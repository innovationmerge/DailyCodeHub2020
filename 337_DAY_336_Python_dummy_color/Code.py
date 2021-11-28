# **************** "iNNovationMerge DailyCodeHub" ****************
# Visit https://www.innovationmerge.com/
# Theme : Dummy Data Generation in Python

# Python program generate dummy color 

from faker import Faker
fake = Faker("en_US")
for _ in range(10):
    print(fake.color_name())



""" 
# Output : 
    Olive
    Aqua
    LightBlue
    Teal
    DarkGreen
    LightSalmon
    DarkSlateBlue
    LightGreen
    MediumOrchid
    LavenderBlush
"""

