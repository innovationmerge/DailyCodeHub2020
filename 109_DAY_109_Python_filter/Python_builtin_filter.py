# "iNNovationMerge DailyCodeHub"

# Theme : Built in week with Python

# Python program to apply filter and get odd numbers

def is_odd(num):  
    if num % 2 == 0:  
        result = False  
    else: 
        result = True  
    return result

f_odd = filter(is_odd, [1,2,3,4,5,6,7,8,9,10,11])  
print(list(f_odd))

# Output : [1, 3, 5, 7, 9, 11]


