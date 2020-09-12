'''3. Write a Python program to add the digits of a positive integer repeatedly until the result has a single digit.
Input : 48
Output : 3
For example given number is 59, the result will be 5.
Step 1: 5 + 9 = 14
Step 1: 1 + 4 = 5 '''

def add_digits(num):
        return (num - 1) % 9 + 1 if num > 0 else 0

print(add_digits(48))
print(add_digits(59))