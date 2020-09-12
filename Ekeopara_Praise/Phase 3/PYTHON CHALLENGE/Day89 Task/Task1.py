'''1. Write a Python program to find the single element appears once in a list where every element appears four times except for one.
Input : [1, 1, 1, 2, 2, 2, 3]
Output : 3 '''

class Solution_once:
    def singleNumber(self, arr):
        ones, twos = 0, 0
        for x in arr:
            ones, twos = (ones ^ x) & ~twos, (ones & x) | (twos & ~x)
        assert twos == 0
        return ones
class Solution_twice:
    def single_number(arr):
        ones, twos, threes = 0, 0, 0
        for x in arr:
            ones, twos, threes = (~x & ones) | (x & ~ones & ~twos & ~threes), (~x & twos) | (x & ones), (~x & threes) | (x & twos)
        return twos

if __name__ == "__main__":
    print(Solution_once().singleNumber([1, 1, 1, 2, 2, 2, 3]))
    print(Solution_once().singleNumber([5, 3, 0, 3, 5, 5, 3]))