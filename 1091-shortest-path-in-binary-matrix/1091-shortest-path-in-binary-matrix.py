class Solution:    
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        q = [(0, 0, 1)]
        if grid[0][0] or grid[n-1][n-1]:
            return -1
        dirs = dirs = [[1,0], [-1,0], [0,1], [0,-1], [-1,-1], [1,1], [1,-1], [-1,1]]
        seen = set()
        while q:
            # print(q)
            i, j, dist = q.pop(0)
            if i == n-1 and j == n-1:
                return dist
            for d1, d2 in dirs:
                x, y = i + d1, j + d2
                if (0 <= x < n and 0 <= y < n) and ((x, y) not in seen) and grid[x][y] == 0:
                    seen.add((x,y))
                    q.append((x, y, dist+1))
            
        return -1
                    
                    
                
                        
        
        