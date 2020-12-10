# "iNNovationMerge DailyCodeHub"
# Python program to Perform  Arthmetic operations using numpy
# pip install numpy

#Import Numpy
import numpy as np
x = np.arange(4)

print("Python Arthmetic operations")
print(x)                        # [0 1 2 3]
print(x+5)                      # [5 6 7 8]
print(x-5)                      # [-5 -4 -3 -2]
print(x*2)                      # [0 2 4 6]
print(x/2)                      # [0.  0.5 1.  1.5]
print(x//2)                     # [0 0 1 1]
print(-x)                       # [ 0 -1 -2 -3]
print(x ** 2)                   # [0 1 4 9]
print(x % 2)                    # [0 1 0 1]
print(-(0.5*x+1) ** 2)          # [-1.   -2.25 -4.   -6.25]
print("\n")                     # 

print("Numpy Arthmetic operations")
print(x)                        # [0 1 2 3]
print(np.add(x,5))              # [5 6 7 8]
print(np.subtract(x,5))         # [-5 -4 -3 -2]
print(np.multiply(x,2))         # [0 2 4 6]
print(np.divide(x,2))           # [0.  0.5 1.  1.5]
print(np.floor_divide(x,2))     # [0 0 1 1]
print(np.negative(x))           # [ 0 -1 -2 -3]
print(np.power(x,2))            # [0 1 4 9]
print(np.mod(x,2))              # [0 1 0 1]