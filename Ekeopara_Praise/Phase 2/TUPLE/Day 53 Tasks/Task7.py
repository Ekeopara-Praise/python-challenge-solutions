'''7. Write a Python program to unzip a list of tuples into individual lists.'''

zipped = [('a', 1), ('b', 2)]
unzipped_obj = list(zip(*zipped))

print(unzipped_obj)