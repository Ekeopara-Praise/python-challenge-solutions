'''3. Write a Python program to find the product xyz.
A Pythagorean triple consists of three positive integers a, b, and c, such that a2 + b2 = c2. Such a triple is commonly written (a, b, c), and a well-known example is (3, 4, 5). There exists exactly one Pythagorean triplet for which x + y + z = 1000.'''

for a in range(1, 1000):
     for b in range(a, 1000):
         c = 1000 - a - b
         if c > 0:
             if c*c == a*a + b*b:
                 print (a*b*c)
                 break


#Reference: w3resource