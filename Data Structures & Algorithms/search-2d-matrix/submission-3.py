class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        T, B = 0, len(matrix) - 1
        i = -1
        while T <= B:
            mid = (T + B) // 2
            if matrix[mid][-1] < target:
                T = mid + 1
            elif matrix[mid][0] > target:
                B = mid - 1
            else:
                i = mid
                break
        
        L, R = 0, len(matrix[0]) - 1
        while L <= R:
            mid = (L + R) // 2
            if matrix[i][mid] < target:
                L = mid + 1
            elif matrix[i][mid] > target:
                R = mid - 1
            else:
                return True
        
        return False
            