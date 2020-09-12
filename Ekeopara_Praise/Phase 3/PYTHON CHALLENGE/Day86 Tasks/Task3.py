'''3. Write a Python program to check if a number is a power of a given base
Input : 128,2
Output : True '''

import math

def isPower (n, base):
    if base == 1 and n != 1:
        return False
    if base == 1 and n == 1:
        return True
    if base == 0 and n != 1:
        return False
    power = int (math.log(n, base) + 0.5)
    return base ** power == n

print(isPower(127,2))
print(isPower(128,2))

print(isPower(27,2))
print(isPower (27,3))
print(isPower (28,3))
print(isPower (2**10,2))
print(isPower (2**12,2))

print(isPower(2,2))
print(isPower(5,5))
print(isPower(10,1))
