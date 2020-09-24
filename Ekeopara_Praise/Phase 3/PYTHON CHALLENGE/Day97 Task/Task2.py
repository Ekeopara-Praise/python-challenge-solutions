'''2. Write a python program to find the 1000th prime number.
A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. By Euclid's theorem, there are an infinite number of prime numbers. Subsets of the prime numbers may be generated with various formulas for primes. The first twenty prime numbers are: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71. '''

count = 0
i = 11

while count <= 1000 and i <= 10000:
    if i%2 != 0:
       if (i%3 == 0 or i%4 == 0 or i%5 == 0 or i%6 == 0 or i%7 == 0 or i%9 == 0):
           continue
       else:
           print i,'is prime.'
           count += 1
    i+=1