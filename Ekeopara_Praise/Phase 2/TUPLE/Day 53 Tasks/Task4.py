'''4. Write a Python program to find the index of an item of a tuple.'''

def find_index(tup, item):
    index_num = tup.index(item)
    return index_num

print(find_index((1, 2, 3, 4, 5), 1))
print(find_index((1, 2, 3, 4, 5), 3))
print(find_index((1, 2, 3, 4, 5), 5))