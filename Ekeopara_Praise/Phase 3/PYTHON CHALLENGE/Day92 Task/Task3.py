'''3. Write a Python program to get the Hamming numbers upto a given numbers also check whether a given number is an Hamming number.
Input : 7
Output : 0
Hamming numbers are numbers of the form
H = 2i x 3j x 5k
Where i, j, k = 0
The sequence of Hamming numbers 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 16, 18, 20, 24, 25, 27. . . consists of all numbers of the form 2i.3j.5k where i, j and k are non-negative integers.
'''

def is_hamming_numbers(x):
	if x == 1:
		return 1
	if x % 2 == 0:
		return is_hamming_numbers(x/2)
	if x % 3 == 0:
		return is_hamming_numbers(x/3)
	if x % 5 == 0:
		return is_hamming_numbers(x/5)
	return 0

def hamming_numbers_sequence(x):
	if x == 1:
		return 1
	hamming_numbers_sequence(x-1)
	if is_hamming_numbers(x) == True:
		print("%s" % x, end=' ')


print(is_hamming_numbers(7))
print(is_hamming_numbers(1))

