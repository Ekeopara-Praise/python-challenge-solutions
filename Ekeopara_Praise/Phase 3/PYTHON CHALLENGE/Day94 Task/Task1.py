'''
1. Write a Python program to find majority element in a list.
Input : [1, 2, 3, 4, 5, 5, 5, 5, 5, 5, 6]
Output : 5
Note: The majority element is the element that appears more than n/2 times where n is the number of elements in the list. '''

l = [1, 2, 3, 4, 5, 5, 5, 5, 5, 5, 6]
print(max(set(l), key = l.count)) 