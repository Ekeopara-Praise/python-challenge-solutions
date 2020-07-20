'''2. Write a Python program to remove an item from a tuple.'''

def remove_item(tup, item):
    lst = list(tup)
    lst.remove(item)
    tupl = tuple(lst)
    return tupl
print(remove_item((1, 2, 3, 4, 5), 3))