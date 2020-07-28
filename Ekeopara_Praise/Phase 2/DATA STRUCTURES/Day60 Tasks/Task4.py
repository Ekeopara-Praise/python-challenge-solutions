'''4. Write a Python program to locate the left insertion point for a specified value in sorted order.
Expected Output:
4
2 '''

import bisect
def index(a, x):
    i = bisect.bisect_left(a, x)
    return i
    
a = [1,2,4,5]
print(index(a, 6))
print(index(a, 3))

#Reference: w3resource