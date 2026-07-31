class Solution:
    def longestPalindrome(self, s: str) -> str:
        # dp=[[0]*len(s) for i in range(len(s))]
        # x,y=0,1
        # for i in range(len(s)):
        #     dp[i][i]=1
        # for i in range(len(s)-1):
        #     if s[i]==s[i+1]:
        #         dp[i][i+1]=1
        #         x=i
        #         y=2
        # for l in range(3,len(s)+1):
        #     for i in range(len(s)-l+1):
        #         j=i+l-1
        #         if s[i]==s[j] and dp[i+1][j-1]==1:
        #             dp[i][j]=1
        #             x=i
        #             y=l
        # return s[x:x+y]
        def check(l,r):
            while l>=0 and r<len(s) and s[l]==s[r]:
                l-=1
                r+=1
            return s[l+1:r]
        op=""
        for i in range(len(s)):
            x=check(i,i)
            y=check(i,i+1)
            op=max(op,x,y,key=len)
        return op