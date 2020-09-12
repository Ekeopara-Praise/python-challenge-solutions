'''2. Write a Python program to find two elements appear twice in a list where all the other elements appear exactly twice in the list.
Input : [1, 2, 1, 3, 2, 5]
Output :[5, 3]'''

import functools
import operator
def two_numbers(arr):
    x_xor_y = functools.reduce(operator.xor, arr)
    bit =  x_xor_y & -x_xor_y
    result = [0, 0]
    for i in arr:
        result[bool(i & bit)] ^= i
    return result

print(two_numbers([1, 2, 1, 3, 2, 5]))
print(two_numbers([11, 5, 3, 7, 0, 5, 3, 6, 7, 11]))
