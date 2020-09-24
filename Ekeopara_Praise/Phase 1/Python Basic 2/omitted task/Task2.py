'''2. Write a Python program to find the operating system name, platform and platform release date.
Operating system name:
posix
Platform name:
Linux
Platform release:
4.4.0-47-generic '''

import os, platform
print("Operating system name:")
print(os.name)
print("Platform name:")
print(platform.system())
print("Platform release:")
print(platform.release())

#Reference: w3resource