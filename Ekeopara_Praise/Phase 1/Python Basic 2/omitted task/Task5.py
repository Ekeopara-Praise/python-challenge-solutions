'''5. Write a Python program to test if a variable is a list or tuple or a set.'''

def check_testVariable(var):
    if type(var) == list:
        reply = "This variable is a List"
    elif type(var) == tuple:
        reply = "This variable is a Tuple"
    elif type(var) == set:
        reply = "This variable is a Set"
    return reply
print(check_testVariable([1, 2, 3, "a"]))
print(check_testVariable(("a", "b", "c")))
print(check_testVariable({1, 2, 3, 4, 5}))