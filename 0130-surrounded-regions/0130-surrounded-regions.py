class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows,cols=len(board),len(board[0])
        def dfs(r,c):
            board[r][c]="D"
            for dr,dc in(1,0),(-1,0),(0,1),(0,-1):
                nr,nc=r+dr,c+dc
                if nr<0 or nr==rows or nc<0 or nc==cols or board[nr][nc]!="O":
                    continue
                dfs(nr,nc)
        for i in [0,rows-1]:
            for j in range(cols):
                if board[i][j]=='O':
                    dfs(i,j)
        for j in [0,cols-1]:
            for i in range(1,rows-1):
                if board[i][j]=="O":
                    dfs(i,j)
        for i in range(rows):
            for j in range(cols):
                if board[i][j]=="O":
                    board[i][j]="X"
                elif board[i][j]=="D":
                    board[i][j]="O"



        