'''2. Write a Python program to check if a given positive integer is a power of three.
Input : 9
Output : True '''

def is_Power_of_three(n):
    while (n % 3 == 0):
         n /= 3;         
    return n == 1

print(is_Power_of_three(9))
print(is_Power_of_three(81))
print(is_Power_of_three(21))

#Reference: w3resource