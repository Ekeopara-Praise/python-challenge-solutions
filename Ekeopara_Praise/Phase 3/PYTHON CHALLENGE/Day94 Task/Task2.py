'''2. Write a Python program to find the length of the last word.
Input : Python Exercises
Output : 9 '''

st1 = 'Python Exercises'

st2 = list(st1.split(" "))
lstval = len(st2[-1])
print(lstval)