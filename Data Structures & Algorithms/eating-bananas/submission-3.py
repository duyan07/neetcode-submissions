import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def eatBananas(k: int) -> bool:
            i = 0
            for j in range(len(piles)):
                i += math.ceil(piles[j] / k)
            return True if i <= h else False

        l, r = 1, max(piles)
        while l < r:
            k = (l + r) // 2
            if eatBananas(k):
                r = k
            else:
                l = k + 1
        return l