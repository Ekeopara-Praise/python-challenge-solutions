'''1. Write a Python program to create a shallow copy of sets.
Note : Shallow copy is a bit-wise copy of an object. A new object is created that has an exact copy of the values in the original object.'''

setp = set(["Red", "Green"])
setq = set(["Green", "Red"])
#A shallow copy
setr = setp.copy()
print(setr)

#Reference: w3resource