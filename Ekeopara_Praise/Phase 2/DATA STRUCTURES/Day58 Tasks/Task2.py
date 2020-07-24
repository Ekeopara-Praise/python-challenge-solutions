'''2. Write a Python program to iterate over an enum class and display individual member and their value.
Expected Output:
Afghanistan = 93
Albania = 355
Algeria = 213
Andorra = 376
Angola = 244
Antarctica = 672 '''

import enum

class Member(enum.Enum):
    Afghanistan = 93
    Albania = 355
    Algeria = 213
    Andorra = 376
    Angola = 244
    Antarctica = 672
    
for i in (Member):
    print(f"Member name: {i.name}")
    print(f"Member value: {i.value}")
    print("")