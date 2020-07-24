'''4. Write a Python program to get all values from an enum class.
Expected output:
[93, 355, 213, 376, 244, 672] '''

import enum
list1 = []
class Member(enum.Enum):
    Afghanistan = 93
    Albania = 355
    Algeria = 213
    Andorra = 376
    Angola = 244
    Antarctica = 672
    
for i in (Member):
    val = i.value
    list1.append(val)

print(list1)