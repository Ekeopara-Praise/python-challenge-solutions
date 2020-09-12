'''
1. Write a Python program to find whether it contains an additive sequence or not.
The additive sequence is a sequence of numbers where the sum of the first two numbers is equal to the third one.
Sample additive sequence: 6, 6, 12, 18, 30
In the above sequence 6 + 6 =12, 6 + 12 = 18, 12 + 18 = 30....
Also, you can split a number into one or more digits to create an additive sequence.
Sample additive sequence: 66121830
In the above sequence 6 + 6 =12, 6 + 12 = 18, 12 + 18 = 30....
Note : Numbers in the additive sequence cannot have leading zeros. '''

class Solution(object):
# DFS: iterative implement.
    def is_additive_number(self, num):
        length = len(num)
        for i in range(1, int(length/2+1)):
            for j in range(1, int((length-i)/2 + 1)):
                first, second, others = num[:i], num[i:i+j], num[i+j:]
                if self.isValid(first, second, others):
                    return True
        return False

    def isValid(self, first, second, others):
        if ((len(first) > 1 and first[0] == "0") or
                (len(second) > 1 and second[0] == "0")):
            return False
        sum_str = str(int(first) + int(second))
        if sum_str == others:
            return True
        elif others.startswith(sum_str):
            return self.isValid(second, sum_str, others[len(sum_str):])
        else:
            return False

if __name__ == "__main__":
    print(Solution().is_additive_number('66121830'))
    print(Solution().is_additive_number('51123'))
    print(Solution().is_additive_number('235813'))