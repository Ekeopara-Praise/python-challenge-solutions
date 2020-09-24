'''6. Write a Python program to find the location of Python module sources.
Operating system name:
posix
Platform name:
Linux
Platform release:
4.4.0-47-generic '''

import sys
print("\nList of directories in sys module:")
print(sys.path)
print("\nList of directories in os module:")
import os
print(os.path)