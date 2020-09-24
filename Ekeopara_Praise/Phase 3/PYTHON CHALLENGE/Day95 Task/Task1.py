'''1. Write a Python program to find the single number which occurs odd 
numbers and other numbers occur even number. '''

def odd_occurrence(arr):
 
    # Initialize result
    result = 0
     
    # Traverse the array
    for element in arr:
        # XOR
        result = result ^ element
 
    return result
 
# Test data
num1 = [ 4, 5, 4, 5, 2, 2, 3, 3, 2, 4, 4 ]
 
print(odd_occurrence(num1))
