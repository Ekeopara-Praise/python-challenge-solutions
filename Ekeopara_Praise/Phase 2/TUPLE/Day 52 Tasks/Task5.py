'''5. Write a Python program to add an item in a tuple.'''

def add_item_to_tuple(tup, item):
    tuplist = list(tup)
    tuplist.append(item)
    tupl = tuple(tuplist)
    return tupl
print(add_item_to_tuple((1, 2, 3, 4), '5678'))