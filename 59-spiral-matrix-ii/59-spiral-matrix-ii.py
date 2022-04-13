class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[0 for _ in range(n)] for _ in range(n)]
        
        i, j, m = 0, 0, n
        
        val = 1
        while i < m and j < n:
            for k in range(j, n):
                ans[i][k] = val
                val += 1
            
            i += 1
            
            for k in range(i, m):
                ans[k][n-1] = val
                val += 1
            
            n -= 1
            
            for k in range(n-1, j-1, -1):
                ans[m-1][k] = val
                val += 1
            
            m -= 1
            
            for k in range(m-1, i-1, -1):
                ans[k][j] = val
                val += 1
            j += 1
        
        return ans
            
            
            
        