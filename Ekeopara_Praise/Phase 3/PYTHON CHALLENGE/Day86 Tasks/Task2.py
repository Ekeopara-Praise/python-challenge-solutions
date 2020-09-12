'''2. Write a Python program to check if an integer is the power of another integer
Input : 16, 2
Output : True '''


import math

# input the numbers
a,b=map(int,input('Enter two values: ').split())

s=math.log(a,b)
p = round(s)

if (b**p)==a:

    print("True")
else:
    print("False")