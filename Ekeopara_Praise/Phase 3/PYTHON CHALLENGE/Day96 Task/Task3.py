'''3. Write a Python program to find the smallest positive number that is evenly divisible by all of the numbers from 1 to 30.
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
Result: 2329089562800.0
''' 

def gcd(x,y): return y and gcd(y, x % y) or x
def lcm(x,y): return x * y / gcd(x,y)

n = 1
for i in range(1, 31):
     n = lcm(n, i)
print(n)
