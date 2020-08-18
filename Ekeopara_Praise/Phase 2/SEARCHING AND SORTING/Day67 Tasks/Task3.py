'''3. Write a Python program to sort a list of elements using Time sort'''

def selection_sort(nums):
    for i, n in enumerate(nums):
        mn = min(range(i,len(nums)), key=nums.__getitem__)
        nums[i], nums[mn] = nums[mn], n
    return nums
user_input = input("Input numbers separated by a comma:\n").strip()
nums = [int(item) for item in user_input.split(',')]
print(selection_sort(nums))

#Reference: w3resource