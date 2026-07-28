from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        fresh = 0
        minutes = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q and fresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in dirs:
                    if (min(r + dr, c + dc) < 0 or
                        r + dr >= len(grid) or c + dc >= len(grid[0]) or
                        grid[r + dr][c + dc] != 1):
                        continue
                    q.append((r + dr, c + dc))
                    grid[r + dr][c + dc] = 2
                    fresh -= 1
            minutes += 1
        
        return minutes if fresh == 0 else -1