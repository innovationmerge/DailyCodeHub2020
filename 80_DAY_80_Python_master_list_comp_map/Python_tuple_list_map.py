# "iNNovationMerge DailyCodeHub"

# Theme : Master List Comprehensions in Python

# Python program to replace map() with List Comprehension

################ map() ##########
technology = ('machine learning', 'data science', 'big data', 'iot', 'embedded')
uppercased_technology_map = list(map(str.upper, technology))
print("map() output", uppercased_technology_map)
# Output : map() output ['MACHINE LEARNING', 'DATA SCIENCE', 'BIG DATA', 'IOT', 'EMBEDDED']

################ List Comprehension ##########
uppercased_technology_list_comp = [tech.upper() for tech in technology]
print("List Comp output", uppercased_technology_list_comp)
# Output : List Comp output ['MACHINE LEARNING', 'DATA SCIENCE', 'BIG DATA', 'IOT', 'EMBEDDED']

