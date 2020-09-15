'''3. Write a Python program to compute the sum of the two reversed numbers and display the sum in reversed form.
Input : 13, 14
Output : 27'''

def reverse_sum(n1, n2):
    return int(str(int(str(n1)[::-1]) + int(str(n2)[::-1]))[::-1])

print(reverse_sum(13, 14))
print(reverse_sum(130, 1))
print(reverse_sum(305, 794))

#Reference: w3resource