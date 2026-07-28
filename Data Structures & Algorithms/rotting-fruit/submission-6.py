from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        mins = 0
        fresh = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                match grid[i][j]:
                    case 2:
                        q.append((i, j))
                    case 1:
                        fresh += 1
        
        dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        while q and fresh > 0:
            for _ in range(len(q)):
                i, j = q.popleft()
                for di, dj in dirs:
                    if (min(i + di, j + dj) < 0 or
                        i + di >= len(grid) or j + dj >= len(grid[0]) or
                        grid[i + di][j + dj] != 1):
                        continue
                    q.append((i + di, j + dj))
                    grid[i + di][j + dj] = 2
                    fresh -= 1
            mins += 1
        
        return mins if fresh == 0 else -1