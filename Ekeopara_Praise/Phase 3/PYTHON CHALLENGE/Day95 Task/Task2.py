'''2. Write a Python program to compute the sum of all the multiples of 3 or 5 below 500.
All the natural numbers below 12 that are multiples of 3 or 5, we get 3, 5, 6, 9 and 10. The sum of these multiples is 33. '''

n = 0
for i in range(1,500):
     if not i % 5 or not i % 3:
         n = n + i
print(n)
