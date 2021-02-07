# "iNNovationMerge DailyCodeHub"

# Theme : Master List Comprehensions in Python

# Python program to convert tuple to list 
# with UPPERCASE using List Comprehensions

################ For loop ##########
technology = ('machine learning', 'data science', 'big data', 'iot', 'embedded')
uppercased_technology_for_loop = []
for tech in technology:
    uppercased_technology_for_loop.append(tech.upper())
print("For loop output", uppercased_technology_for_loop)
# Output : ['MACHINE LEARNING', 'DATA SCIENCE', 'BIG DATA', 'IOT', 'EMBEDDED']

################ List Comprehension ##########
uppercased_technology_list_comp = [tech.upper() for tech in technology]
print("List Comp output", uppercased_technology_list_comp)
# Output : ['MACHINE LEARNING', 'DATA SCIENCE', 'BIG DATA', 'IOT', 'EMBEDDED']

