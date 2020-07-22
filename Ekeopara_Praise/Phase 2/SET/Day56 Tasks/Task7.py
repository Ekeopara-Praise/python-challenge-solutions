'''7. Write a Python program to check if two given sets have no elements in common.'''

try:
    set1 = {4, 9, 5}
    set2 = {4, 3, 5}
    print(set1 & set2)
except:
    print("No value in common")