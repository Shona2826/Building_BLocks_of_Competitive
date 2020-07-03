class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """                                                       
        def dfs(board,i,j):
            
            if board[i][j] == 'O':
                
                board[i][j] = '1'
                if  i+1 < len(board):
                    dfs(board,i+1,j)
                if i>1:
                    dfs(board,i-1,j)
                if j+1 < len(board[i]):
                    dfs(board,i,j+1)
                if j > 1:
                    dfs(board,i,j-1)
                    
        if len(board) == 0 or len(board[0]) == 0:
            return board
                
        row = len(board)
        col = len(board[0])
        for i in range(row):
            dfs(board,i,0)
            dfs(board,i,col-1)
        for j in range(1,col-1):
            dfs(board,0,j)
            dfs(board,row-1,j)
        
            
        for i in range(row):
            for j in range(col):
                
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '1':
                    board[i][j] = 'O'
                    
        