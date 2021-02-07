# "iNNovationMerge DailyCodeHub"

# Theme : Master List Comprehensions in Python

# Python program to apply conditional statement in List Comprehensions

################ For loop ##########
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
squared_primes = []
for prime in primes:
    if prime%10 == 3:
        squared_primes.append(prime*prime)
print("For loop output :", squared_primes)
# Output : For loop output : [9, 169, 529]


################ List Comprehension ##########
squared_primes = [x*x for x in primes if x%10 == 3]
print("List comp output : ", squared_primes)
# List comp output :  [9, 169, 529]
