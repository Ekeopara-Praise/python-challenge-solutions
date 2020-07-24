'''10. Write a Python program to group a sequence of key-value pairs into a dictionary of lists.
Expected output:
[('v', [1, 3]), ('vi', [2, 4]), ('vii', [1])] '''

from collections import defaultdict
class_roll = [('v', 1), ('vi', 2), ('v', 3), ('vi', 4), ('vii', 1)]
d = defaultdict(list)
for k, v in class_roll:
    d[k].append(v)
print(sorted(d.items()))

#Reference: w3resource