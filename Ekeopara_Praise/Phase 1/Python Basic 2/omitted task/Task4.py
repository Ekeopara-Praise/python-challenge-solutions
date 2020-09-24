'''4. Write a Python program to check whether variable is of integer or string.'''

def checkvariable(var):
    if type(var) == int:
        ans = f'{var} is an integer value'
    elif type(var) == str:
        ans = f'\'{var}\' is a string value'
    else:
        ans = 'You know the answer'
    return ans
print(checkvariable(12))
print(checkvariable("abc"))