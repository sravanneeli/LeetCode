class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low = 0
        m = len(matrix)
        n = len(matrix[0])
        high = m * n - 1
        
        while low <= high:
            mid = low + (high - low) // 2
            
            if matrix[mid//n][mid%n] == target:
                return True
            elif matrix[mid//n][mid%n] < target:
                low = mid + 1
            else:
                high = mid - 1
        
        return False