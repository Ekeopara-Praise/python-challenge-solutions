'''2. Write a Python program to read a file line by line and store it into a list.'''

def line_by_line(filename):

    with open(filename) as f:
        content = f.readlines()
    content = [x.strip() for x in content]

    return content 