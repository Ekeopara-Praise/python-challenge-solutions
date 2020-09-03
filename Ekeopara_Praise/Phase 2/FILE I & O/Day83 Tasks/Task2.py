'''2. Write a Python program to remove newline characters from a file. '''

filename = 'examples/files/numbers.txt'

with open(filename, 'r') as fh:
    for line in fh:
        line = line.rstrip("\n")
        print(line)