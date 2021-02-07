# "iNNovationMerge DailyCodeHub"

# Theme : Master List Comprehensions in Python

# Python program to convert tuple to list with UPPERCASE 
# Generate unique elements using NESTED SET List Comprehensions

################ For loop and SET ##########
technology = (('machine learning', 'data science','big data'), ('big data', 'iot', 'embedded'))
uppercased_technology_for_loop = []
for tech_items in technology:
    for tech in tech_items: 
        uppercased_technology_for_loop.append(tech.upper())
print("For loop SET output", set(uppercased_technology_for_loop))
# For loop SET output ['MACHINE LEARNING', 'DATA SCIENCE', 'BIG DATA', 'IOT', 'EMBEDDED']

################ Nested SET List Comprehension ##########
uppercased_technology_list_comp = list({x.upper() for tech in technology for x in tech})
print("Nested List Comp SET output", uppercased_technology_list_comp)
# Nested List Comp SET output ['MACHINE LEARNING', 'DATA SCIENCE', 'BIG DATA', 'IOT', 'EMBEDDED']

