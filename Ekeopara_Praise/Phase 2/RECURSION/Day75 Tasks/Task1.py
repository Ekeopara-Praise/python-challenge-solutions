'''1. Write a Python program to get the factorial of a non-negative integer. '''

def facto(num):

    ans = 1
    if num < 0:
        ans = 'Not a positive number'
    elif num == 0:
        ans = 1 

    else:
        while num >= 1:
            ans = ans * num
            num = num - 1
    return ans

print(facto(5))