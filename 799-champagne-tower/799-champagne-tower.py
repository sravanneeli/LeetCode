class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        tower = [[0] * i for i in range(1, 102)]
        tower[0][0] = poured
        for r in range(query_row+1):
            for c in range(r+1):
                q = (tower[r][c] - 1.0) / 2.0
                if q > 0:
                    tower[r+1][c] += q
                    tower[r+1][c+1] += q
        
        return min(1.0, tower[query_row][query_glass])
        