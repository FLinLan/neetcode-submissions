class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        L, R = 0, ROWS*COLS - 1
        
        while L <= R:
            mid = (L + R) // 2
            row, col = mid // COLS, mid % COLS
            
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                L = mid + 1
            else:
                R = mid - 1
        
        return False
        