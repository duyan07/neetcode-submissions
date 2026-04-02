class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if h == 1:
            return piles[0]

        def canFinish(k):
            return sum((pile + k - 1) // k for pile in piles) <= h
        
        l = 1
        r = max(piles)

        while l <= r:
            k = (l + r) // 2
            if canFinish(k):
                r = k - 1
            else:
                l = k + 1
        
        return l