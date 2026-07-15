import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 0: return 0

        heap = stones[:]
        heapq.heapify_max(heap)

        while len(heap) > 1:
            x = heapq.heappop_max(heap)
            y = heapq.heappop_max(heap)
            if x != y:
                heapq.heappush_max(heap, abs(x - y))
        
        return heap[0] if heap else 0