'''1. Write a Python program to assess if a file is closed or not.'''

f = open('file.py')
if f.closed:
  print('file is closed')
else:
    print('file is still open')