 
# Check if given array is Monotonic 
def isMonotonic(A): 
  
    return (all(A[i] <= A[i + 1] for i in range(len(A) - 1)) or
            all(A[i] >= A[i + 1] for i in range(len(A) - 1))) 
  
# Driver program 
A = [6, 5, 4, 4] # Output - True
B = [6, 5, 4, 6] # Output - False

# Print required result 
print(isMonotonic(A)) 
print(isMonotonic(B)) 

# This code is written by 
# Sanjit_Prasad 