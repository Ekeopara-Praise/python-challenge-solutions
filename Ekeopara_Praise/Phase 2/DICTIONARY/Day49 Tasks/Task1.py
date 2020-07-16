'''1. Write a Python program to multiply all the items in a dictionary.'''

dict1 = {'a': 2, 'b': 3, 'c': 34}
mult = 1
for i in dict1:
    mult = mult*dict1[i]
print(mult)