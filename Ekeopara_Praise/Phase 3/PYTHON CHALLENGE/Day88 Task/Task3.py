'''3. Write a Python program to find the single number in a list that doesn't occur twice
Input : [5, 3, 4, 3, 4]
Output : 5
'''

def single_number(arr):
    result = 0
    for i in arr:
        result ^= i
    return result

arr1 = [5, 3, 4, 3, 4]
arr2 = [3, 2, 5, 2, 1, 5, 3]

print(single_number(arr1))
print(single_number(arr2))
