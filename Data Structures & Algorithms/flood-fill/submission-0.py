class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        og = image[sr][sc]

        def flood(i, j):
            if (min(i, j) < 0 or
                i == len(image) or j == len(image[0]) or
                image[i][j] == color or image[i][j] != og):
                return
            
            image[i][j] = color
            flood(i, j - 1)
            flood(i, j + 1)
            flood(i - 1, j)
            flood(i + 1, j)
        
        flood(sr, sc)
        return image