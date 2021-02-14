# "iNNovationMerge DailyCodeHub"

# Theme : One liner week with Python

# Python program to check if string is palindrome or not in one line

################ For loop  ##########
def is_palindrome(string):
    if string == string[::-1]:
        return True
    else:
        return False
print("For loop output : ", is_palindrome("abcba"))
# For loop output :  True

################ One liner ##########
string = "abcba"
print("One liner output : ",string == string[::-1] ) 
# One liner output :  True



