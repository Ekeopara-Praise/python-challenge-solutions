'''1. Write a Python program to create an Enum object and display a member name and value.
Sample data :
Afghanistan = 93
Albania = 355
Algeria = 213
Andorra = 376
Angola = 244
Antarctica = 672
Expected Output :
Member name: Albania
Member value: 355 '''

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