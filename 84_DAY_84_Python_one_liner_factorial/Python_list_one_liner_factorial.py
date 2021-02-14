# "iNNovationMerge DailyCodeHub"

# Theme : One liner week with Python

# Python program to Find factorial of a number in one line

################ For loop  ##########
def fact(n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1)
print("For loop factorial : ", fact(5))
# For loop factorial :  120

################ One liner ##########
from functools import reduce
n = 5
print("One liner factorial : ",reduce(lambda x, y: x*y, range(1, n+1)))
# One liner factorial :  120

