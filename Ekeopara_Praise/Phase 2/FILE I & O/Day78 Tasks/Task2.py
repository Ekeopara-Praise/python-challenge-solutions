'''2. Write a Python program to read first n lines of a file.'''

def read_file(myfile, num):
    for i in range(num):
        line = myfile.readline()
    return line
print(read_file("Just so you know.txt", 2))