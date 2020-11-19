# Square the numbers in the list.
import math
  
if __name__ == '__main__':
  arr = [1, 2, 3, 4, 5]
  arr = list(map(lambda x : x**2, arr))
  print (arr)
  # prints [1, 4, 9, 16, 25]