'''1. Write a Python program to find a missing number from a list.
Input : [1,2, 3,4,6,7,8]
Output : 5 '''

lst = [1,2,3,4,6,7,8]

a = lst[0]
b = lst[-1]

complete_list = list(range(a, b+1))
missing_number = set(complete_list) ^ set(lst)

print(missing_number)
