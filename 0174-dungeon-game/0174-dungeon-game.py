class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m=len(dungeon)
        n=len(dungeon[0])
        dp=[[0]*n for i in range(m)]
        dp[m-1][n-1]=max(1,1-dungeon[m-1][n-1])

        for i in range(m-2,-1,-1):
            dp[i][n-1]=max(1,dp[i+1][n-1]-dungeon[i][n-1])
        for i in range(n-2,-1,-1):
            dp[m-1][i]=max(1,dp[m-1][i+1]-dungeon[m-1][i])
        for i in range(m-2,-1,-1):
            for j in range(n-2,-1,-1):
                x=min(dp[i+1][j],dp[i][j+1])-dungeon[i][j]
                dp[i][j]=max(1,x)
        return dp[0][0]
        



