'''1. Write a Python program to compare two unordered lists (not sets).
Expected Output: False '''

import collections
compare = lambda x, y: collections.Counter(x) == collections.Counter(y)


print(compare([1,2,3], [1,2,3,3]))
print(compare([1,2,3], [1,2,3]))
print(compare([1,2,3,3], [1,2,2,3]))