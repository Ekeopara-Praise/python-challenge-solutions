'''3. Write a Python program to determine if the python shell is executing in 32bit or 64bit mode 
on operating system.'''


# For 32 bit it will return 32 and for 64 bit it will return 64
import struct
print(struct.calcsize("P") * 8)