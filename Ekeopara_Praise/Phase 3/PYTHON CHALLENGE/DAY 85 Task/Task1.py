'''1. Write a Python program to check if a given positive integer is a power of two.
Input : 4
Output : True'''

def is_power_of_two(n):
    """Return True if n is a power of two."""
    if n <= 0:
        return False
    else:
        return n & (n - 1) == 0
 
 
n = int(input('Enter a number: '))
 
if is_power_of_two(n):
    print("True")
else:
    print("False")

