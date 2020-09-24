'''1. Write a python program to find the difference between the sum of the squares of the first two hundred natural numbers and the square of the sum.
The sum of the squares of the first twenty natural numbers is,
12+22+32+.....+202 = 2870
The square of the sum of the first twenty natural numbers is,
(1 + 2 + ... + 10)2 = 44100
Hence the difference between the sum of the squares of the first twenty natural numbers and the square of the sum is 44100 - 2870 = 41230 Output: 401323300 '''

r = range(1, 201)
a = sum(r)
print (a * a - sum(i*i for i in r))
