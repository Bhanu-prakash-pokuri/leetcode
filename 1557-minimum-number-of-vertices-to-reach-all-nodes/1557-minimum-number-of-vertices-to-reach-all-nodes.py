class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        c=[0]*(n)
        l=[]
        for i,j in edges:
            c[j]+=1
        for i in range(len(c)):
            if c[i]==0:
                l.append(i)
        return l