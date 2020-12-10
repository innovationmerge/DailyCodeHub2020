# "iNNovationMerge DailyCodeHub"

# Python program to create single and multidiemnstional arrays using numpy

# pip install numpy

#Import Numpy
import numpy as np

result = np.zeros(20, dtype="int") #Integer array filled with zeros
print(result,result.dtype,"\n")
# [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0] int32    

result = np.zeros((6,10), dtype="float") #Integer array filled with zeros
print(result,result.dtype,"\n")
"""
 [[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]] float64
 """

result = np.ones((4,12), dtype="float") #float array filled with 1s
print(result,result.dtype,"\n")
"""
[[1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]] float64
"""    

result = np.full((6,4), 4.15) #float array filled with 4.15
print(result,result.dtype,"\n")
"""
[[4.15 4.15 4.15 4.15]
 [4.15 4.15 4.15 4.15]
 [4.15 4.15 4.15 4.15]
 [4.15 4.15 4.15 4.15]
 [4.15 4.15 4.15 4.15]
 [4.15 4.15 4.15 4.15]] float64
"""    

result = np.arange(0,40,3) #array filled with a linear sequence, stepping by 3
print(result,result.dtype,"\n")
# [ 0  3  6  9 12 15 18 21 24 27 30 33 36 39] int32

result = np.linspace(0,2,5) #array of five values evenly spaced between 0 and 2
print(result,result.dtype,"\n")
# [0.  0.5 1.  1.5 2. ] float64