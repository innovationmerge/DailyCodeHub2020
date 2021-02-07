# "iNNovationMerge DailyCodeHub"

# Theme : Master List Comprehensions in Python

# Python program to convert tuple to list with UPPERCASE using NESTED List Comprehensions

################ For loop ##########
technology = (('machine learning', 'data science'), ('big data', 'iot', 'embedded'))
uppercased_technology_for_loop = []
for tech_items in technology:
    for tech in tech_items: 
        uppercased_technology_for_loop.append(tech.upper())
print("For loop output", uppercased_technology_for_loop)
# For loop output ['MACHINE LEARNING', 'DATA SCIENCE', 'BIG DATA', 'IOT', 'EMBEDDED']

################ Nested List Comprehension ##########
uppercased_technology_list_comp = [x.upper() for tech in technology for x in tech]
print("Nested List Comp output", uppercased_technology_list_comp)
# Nested List Comp output ['MACHINE LEARNING', 'DATA SCIENCE', 'BIG DATA', 'IOT', 'EMBEDDED']

