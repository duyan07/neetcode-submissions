# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        if n == 1:
            return n

        l = 0
        r = n
        
        while l <= r:
            pick = (l + r) // 2
            is_correct = guess(pick)
            if is_correct == 1:
                l = pick + 1
            elif is_correct == -1:
                r = pick - 1
            else:
                return pick
