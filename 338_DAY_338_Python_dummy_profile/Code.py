# **************** "iNNovationMerge DailyCodeHub" ****************
# Visit https://www.innovationmerge.com/
# Theme : Dummy Data Generation in Python

# Python program generate dummy profile 

from faker import Faker
fake = Faker("en_US")
for _ in range(1):
    print(fake.profile())



""" 
# Output : 
    {'job': 'Software engineer', 'company': 'Harper LLC', 'ssn': '794-55-5559', 'residence': '67153 Campbell Crossing Suite 100\nNew Johnnyside, ID 22558', 'current_location': (Decimal('62.784573'), Decimal('126.810257')), 'blood_group': 'O-', 'website': ['https://ruiz.com/'], 'username': 'stephaniethornton', 'name': 'Pamela Barajas', 'sex': 'F', 'address': '8692 Kelsey Views\nPort Davidchester, MN 79032', 'mail': 'jenkinsrenee@yahoo.com', 'birthdate': datetime.date(2021, 1, 8)}
"""

