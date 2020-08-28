'''1. Write a Python program to read a file line by line store it into an array.'''

testsite_array = []
with open('topsites.txt') as my_file:
    for line in my_file:
        testsite_array.append(line)