class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        g.sort()
        s.sort()
        ans=0
        i=j=0
        while i<len(g) and j<len(s):
            if s[j]>=g[i]:
                i+=1
                j+=1
                ans+=1
            else:
                j+=1
        return ans