'''8. Write a Python program to read a string and interpreting the string as an array of machine values.
Expected Output:
array1: array('i', [7, 8, 9, 10])
Bytes: b'0700000008000000090000000a000000'
array2: array('i', [7, 8, 9, 10]) '''

from array import array
import binascii
array1 = array('i', [7, 8, 9, 10])
print('array1:', array1)
as_bytes = array1.tobytes()
print('Bytes:', binascii.hexlify(as_bytes))
array2 = array('i')
array2.frombytes(as_bytes)
print('array2:', array2)