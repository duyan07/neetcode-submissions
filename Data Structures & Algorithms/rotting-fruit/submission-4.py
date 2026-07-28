from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        minutes = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i, j))

        while q:
            for k in range(len(q)):
                r, c = q.popleft()

                dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for dr, dc in dirs:
                    if (min(r + dr, c + dc) >= 0 and
                        r + dr < len(grid) and c + dc < len(grid[0]) and
                        grid[r + dr][c + dc] == 1):
                        q.append((r + dr, c + dc))
                        grid[r + dr][c + dc] = 2
            if q:
                minutes += 1
                
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        
        return minutes if minutes > 0 else 0