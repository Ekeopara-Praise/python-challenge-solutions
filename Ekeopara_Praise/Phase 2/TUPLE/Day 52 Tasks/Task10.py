'''10. Write a Python program to check whether an element exists within a tuple.'''

def check_in_tuple(tup, item):
    if item in tup:
        ans = 'True'
    else:
        ans = 'False'
    return ans
print(check_in_tuple((1, 2, 3, 4, 5), 3))
print(check_in_tuple((1, 2, 3, 4, 5), 4))
print(check_in_tuple((1, 2, 3, 4, 5), 0))