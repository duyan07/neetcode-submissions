class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if h == 1:
            return piles[0]

        def eat(piles, k, h):
            hours_needed = 0
            for pile in piles:
                hours_needed += (pile + k - 1) // k
            return h - hours_needed
        
        l = 1
        r = max(piles)
        min_k = r

        while l <= r:
            k = (l + r) // 2
            hours_needed = eat(piles, k, h)
            if hours_needed >= 0:
                r = k - 1
                min_k = k
            elif hours_needed < 0:
                l = k + 1
        
        return min_k