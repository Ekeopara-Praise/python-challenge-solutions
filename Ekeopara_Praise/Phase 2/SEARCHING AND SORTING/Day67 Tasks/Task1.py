'''
1. Write a Python program to sort a list of elements using Radix sort.
According to Wikipedia "In computer science, radix sort is a non-comparative integer
 sorting algorithm that sorts data with integer keys by grouping keys by the individual digits which share 
 the same significant position and value". '''

def radix_sort(nums):
    RADIX = 10
    placement = 1
    max_digit = max(nums)

    while placement < max_digit:
      buckets = [list() for _ in range( RADIX )]
      for i in nums:
        tmp = int((i / placement) % RADIX)
        buckets[tmp].append(i)
      a = 0
      for b in range( RADIX ):
        buck = buckets[b]
        for i in buck:
          nums[a] = i
          a += 1
      placement *= RADIX
    return nums
user_input = input("Input numbers separated by a comma:\n").strip()
nums = [int(item) for item in user_input.split(',')]
print(radix_sort(nums))

#Reference: w3resource