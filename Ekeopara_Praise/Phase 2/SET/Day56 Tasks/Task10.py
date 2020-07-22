'''10. Write a Python program to check a given set has no elements in common with other given set.'''

try:
    set1 = {4, 9, 5}
    set2 = {4, 3, 5}
    print(set1 & set2)
except:
    print("No value in common")