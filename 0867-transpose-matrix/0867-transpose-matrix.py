class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        m=len(matrix)
        n=len(matrix[0])
        res=[[0]*m for i in range(n)]
        for i in range(n):
            for j in range(m):
                res[i][j]=matrix[j][i]
        return res