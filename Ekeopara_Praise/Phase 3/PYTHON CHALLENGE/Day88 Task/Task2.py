'''2. Write a Python program to compute and return the square root of a given 'integer'.
Input : 16
Output : 4
Note : The returned value will be an 'integer' '''

# Returns floor of square root of x 
def floorSqrt(x): 
  
    # Base cases 
    if (x == 0 or x == 1): 
        return x 
  
    # Staring from 1, try all numbers until 
    # i*i is greater than or equal to x. 
    i = 1; result = 1
    while (result <= x): 
      
        i += 1
        result = i * i 
      
    return i - 1
  
# Driver Code 
x = 11
print(floorSqrt(x)) 