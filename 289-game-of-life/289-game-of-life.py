class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        dirs = [[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1]]
        for i in range(m):
            temp = []
            for j in range(n):
                lives = 0
                for r,c in dirs:
                    nr, nc = i + r, j + c
                    if (0 <= nr < m and 0 <= nc < n) and abs(board[nr][nc]) == 1:
                        lives += 1
                        
                if board[i][j] == 1:
                    if lives < 2 or lives > 3:   
                        board[i][j] = -1
                else:
                    if lives == 3:  
                        board[i][j] = 2
                # print(board)
                
        for i in range(m):
            for j in range(n):
                if board[i][j] == 2:    board[i][j] = 1
                elif board[i][j] == -1: board[i][j] = 0
                    