class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def search(i, j):
            if (min(i, j) < 0 or
                i == len(grid) or j == len(grid[0]) or
                grid[i][j] == 0):
                return 0

            grid[i][j] = 0
            area = 1
            area += search(i, j - 1)
            area += search(i, j + 1)
            area += search(i - 1, j)
            area += search(i + 1, j)
            return area
        
        maxArea = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                maxArea = max(maxArea, search(i, j))
        
        return maxArea
        