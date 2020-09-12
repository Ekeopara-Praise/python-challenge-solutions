'''3. Write a Python program to reverse the bits of an integer (32 bits unsigned).
Input : 1234
Output : 1260388352
For example, 1234 represented in binary as 10011010010 and returns 1260388352 which represents in binary as 1001011001000000000000000000000. '''

def reverse_Bits(n):
        result = 0
        for i in range(32):
            result <<= 1
            result |= n & 1
            n >>= 1
        return result
            
print(reverse_Bits(1234))