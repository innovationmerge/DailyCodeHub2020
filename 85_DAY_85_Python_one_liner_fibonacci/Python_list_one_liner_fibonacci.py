# "iNNovationMerge DailyCodeHub"

# Theme : One liner week with Python

# Python program to Find Fibonacci of a number in one line

################ For loop  ##########
def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
print("For loop output : ", fib(5))
# For loop output :  5

################ One liner ##########
fib_one = lambda x: x if x<=1 else fib(x-1) + fib(x-2)
print("One liner output : ", fib_one(5)) 
# One liner output :  5

