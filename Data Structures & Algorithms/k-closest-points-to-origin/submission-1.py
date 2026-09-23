import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dists = []
        for x, y in points:
            dist = x * x + y * y
            heapq.heappush_max(dists, (dist, x, y))
            if len(dists) > k:
                heapq.heappop_max(dists)
        
        return [[x, y] for (_, x, y) in dists]
        
        
