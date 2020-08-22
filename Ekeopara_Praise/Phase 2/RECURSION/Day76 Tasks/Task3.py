'''3. Write a Python program to calculate the geometric sum of n-1.
Note: In mathematics, a geometric series is a series with a constant ratio between successive terms.
Example :A harmonic series: 1+1/2+1/3+1/4+1/5........ '''

def geometric_sum(n):
  if n < 0:
    return 0
  else:
    return 1 / (pow(2, n)) + geometric_sum(n - 1)
 
print(geometric_sum(7))
print(geometric_sum(4))