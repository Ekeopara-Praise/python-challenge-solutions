'''2. Write a Python program to solve the Fibonacci sequence using recursion. '''

term = int(input("Eneter the number of terms? "))
n1, n2, count = 0, 1, 2

if term== 1:
    print("The Sequence is: ", n1)
elif term <0:
    print("Please enter a valid positive number !!")
else:
    arr1 = []
    arr1.append(n1)
    arr1.append(n2)
    while count< term:
        nth = n1 + n2
        arr1.append(nth)
        n1 = n2
        n2 = nth
        count += 1
print("The Sequence: ", arr1) 