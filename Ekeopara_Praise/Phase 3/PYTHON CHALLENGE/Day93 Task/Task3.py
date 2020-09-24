'''3. Write a Python program to the push the first number to the end of a list. '''

lst = [2, 3, 4, 6, 7, 10, 0]
a = lst.pop(0)
answer = lst.append(a)
print(lst)