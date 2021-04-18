# "iNNovationMerge DailyCodeHub"

# Theme : Debug week with Python

# Debugging Python code using pdb

def divide_func(a, b):
    import pdb; pdb.set_trace()
    result = a / b
    return result
  
print(divide_func(5, 0))

"""Commands for debugging
c - Continue Execution
n - Go to next line within same method
s - Go to next line in a called method
q - Quit debugging
"""

