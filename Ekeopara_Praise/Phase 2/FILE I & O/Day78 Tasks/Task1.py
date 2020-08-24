'''1. Write a Python program to read an entire text file.'''


def read_file(myfile):
    docum = open(myfile)
    return docum.read()
print(read_file(r"C:\Users\Sir_Praise\Desktop\47 to 51.txt"))