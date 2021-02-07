# "iNNovationMerge DailyCodeHub"

# Theme : Master List Comprehensions in Python

# Python program to use function in List Comprehensions

def upperCaseElements(element):
    return element.upper()

################ For loop ##########
technology = ('machine learning', 'data science', 'big data', 'iot', 'embedded')
uppercased_technology_for_loop = []
for tech in technology:
    uppercased_technology_for_loop.append(upperCaseElements(tech))
print("For loop output", uppercased_technology_for_loop)
# Output : For loop output ['MACHINE LEARNING', 'DATA SCIENCE', 'BIG DATA', 'IOT', 'EMBEDDED']

################ List Comprehension ##########
uppercased_technology_list_comp = [upperCaseElements(tech) for tech in technology]
print("List Comp output", uppercased_technology_list_comp)
# Output : List Comp output ['MACHINE LEARNING', 'DATA SCIENCE', 'BIG DATA', 'IOT', 'EMBEDDED']

