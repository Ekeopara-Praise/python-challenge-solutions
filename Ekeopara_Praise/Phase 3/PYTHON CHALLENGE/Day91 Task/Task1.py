'''1. Write a Python program to check a sequence of numbers is an arithmetic progression or not.
Input : [5, 7, 9, 11]
Output : True
In mathematics, an arithmetic progression or arithmetic sequence is a sequence of numbers such that the difference between the
 consecutive terms is constant.
For example, the sequence 5, 7, 9, 11, 13, 15 ... is an arithmetic progression with common difference of 2. '''

def progression(l):

    if len(l) == 1:
        return True
    else:

        diff = l[1] - l[0]
        for index in range(len(l) - 1):
            if not (l[index + 1] - l[index] == diff):
                return False
        return True


print(progression([7, 3, -1, -5]))
print(progression([5, 7, 9, 11]))