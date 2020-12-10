# "iNNovationMerge DailyCodeHub"
# Python program to Perform  Trigonometric operations using numpy
# pip install numpy

#Import Numpy
import numpy as np

#Trigonmetric functions
print("Trigonometric functions")                #
x = np.linspace(0,np.pi,3)                      #

print(x)                                        # [0.         1.57079633 3.14159265]
print(np.sin(x))                                # [0.0000000e+00 1.0000000e+00 1.2246468e-16]
print(np.cos(x))                                # [ 1.000000e+00  6.123234e-17 -1.000000e+00]
print(np.tan(x))                                # [ 0.00000000e+00  1.63312394e+16 -1.22464680e-16]
print("\n")                                

#Trigonmetric functions on arrays
print("Trigonometric functions on arrays")
x = [-1,0,1]
print(x)                                        # [-1, 0, 1]
print(np.arcsin(x))                             # [-1.57079633  0.          1.57079633]
print(np.arccos(x))                             # [3.14159265 1.57079633 0.        ]
print(np.arctan(x))                             # [-0.78539816  0.          0.78539816]