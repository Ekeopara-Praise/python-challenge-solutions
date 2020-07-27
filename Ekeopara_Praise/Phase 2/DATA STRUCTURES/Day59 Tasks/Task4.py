'''4. Write a Python program to get an array buffer information.
Expected Output:
Array buffer start address in memory and number of elements.
(25855056, 2) '''

from array import array
a = array("I", (12,25))
print("Array buffer start address in memory and number of elements.")
print(a.buffer_info())


#Reference: w3resource