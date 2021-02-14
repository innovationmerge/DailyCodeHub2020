# "iNNovationMerge DailyCodeHub"

# Theme : One liner week with Python

# Python program to reverse a list in one line

################ For loop  ##########
ls = [1, 2, 3]
ls_comp = []
for i in range(1, len(ls)+1):
    ls_comp.append(ls[len(ls)-i])
print("For loop output : ", ls_comp)
# For loop output :  [3, 2, 1]

################ One liner ##########
ls = [1, 2, 3]
ls.reverse()
print("One liner output : ", ls) 
# One liner output :  [3, 2, 1]




