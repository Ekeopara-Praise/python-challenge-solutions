'''5. Write a Python program to count the most common words in a dictionary.
Expected Output:
[('pink', 6), ('black', 5), ('white', 5), ('red', 4)] '''

from collections import Counter

lst1 = ['pink', 'pink', 'pink', 'pink', 'pink', 'black', 'black', 'black', 'red', 'red', 'red']
print(Counter(lst1).most_common())