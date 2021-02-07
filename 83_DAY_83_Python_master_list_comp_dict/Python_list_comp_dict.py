# "iNNovationMerge DailyCodeHub"

# Theme : Master List Comprehensions in Python

# Python program to convert tuple to list with UPPERCASE 
# Generate word count using NESTED List Comprehensions

################ For loop and SET ##########
technology = (('machine learning', 'data science','big data'), ('big data', 'iot', 'embedded'))
uppercased_technology_for_loop = {}
for tech_items in technology:
    for tech in tech_items: 
        uppercased_technology_for_loop[tech.upper()] = len(tech)
print("For loop dict output", uppercased_technology_for_loop)
# For loop dict output {'MACHINE LEARNING': 16, 'DATA SCIENCE': 12, 'BIG DATA': 8, 'IOT': 3, 'EMBEDDED': 8}

################ Nested SET List Comprehension ##########
uppercased_technology_list_comp = {x.upper() : len(x) for tech in technology for x in tech}
print("Nested List Comp dict output", uppercased_technology_list_comp)
# Nested List Comp dict output {'MACHINE LEARNING': 16, 'DATA SCIENCE': 12, 'BIG DATA': 8, 'IOT': 3, 'EMBEDDED': 8}

