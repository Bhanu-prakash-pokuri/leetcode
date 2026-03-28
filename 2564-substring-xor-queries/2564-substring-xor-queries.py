class Solution:
    def substringXorQueries(self, s: str, queries: List[List[int]]) -> List[List[int]]:
        occur={}
        n=len(s)
        for i in range(n):
            if s[i]=='0':
                if 0 not in occur:
                    occur[0]=[i,i]
                continue
            v=0
            for j in range(i,min(i+30,n)):
                v=v*2+int(s[j])
                if v not in occur:
                    occur[v]=[i,j]
        res=[]
        for i,j in queries:
            t=i^j
            if t in occur:
                res.append(occur[t])
            else:
                res.append([-1,-1])
        return res 
        