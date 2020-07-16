'''5. Write a Python program to get the maximum and minimum value in a dictionary '''

dict1 = {'a': 2, 'b': 3, 'c': 34}

Maxi = max(dict1, key=dict1.get)
Mini = min(dict1, key=dict1.get)
print(Maxi)
print(Mini)