'''3. Write a Python program to get the sum of a non-negative integer.
Test Data:
sumDigits(345) -> 12
sumDigits(45) -> 9 '''

def sumDigits(n):
  if n == 0:
    return 0
  else:
    return n % 10 + sumDigits(int(n / 10))

print(sumDigits(345))
print(sumDigits(45))