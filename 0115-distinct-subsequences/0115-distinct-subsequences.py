class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n=len(t)
        l=[0]*(n+1)
        l[0]=1
        for i in range(len(s)):
            for j in range(n-1,-1,-1):
                if s[i]==t[j]:
                    l[j+1]+=l[j]
        return l[n]

        