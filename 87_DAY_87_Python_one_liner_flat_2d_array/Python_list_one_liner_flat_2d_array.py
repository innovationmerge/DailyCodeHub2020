# "iNNovationMerge DailyCodeHub"

# Theme : One liner week with Python

# Python program to flatten a 2-D array in one line

################ For loop  ##########
ls = [[1, 2], [3, 4], [5, 6]]
ls2 = []
for i in ls:
    for j in i:
        ls2.append(j)
print("For loop output : ", ls2)
# For loop output :  [1, 2, 3, 4, 5, 6]

################ One liner ##########
ls = [[1, 2], [3, 4], [5, 6]]
print("One liner output : ",[i for j in ls for i in j]) 
# One liner output :  [1, 2, 3, 4, 5, 6]




