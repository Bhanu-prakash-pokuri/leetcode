class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        g=defaultdict(list)
        if n==1:
            return [0]
        ind=[0]*n
        for x,y in edges:
            g[x].append(y)
            g[y].append(x)
            ind[x]+=1
            ind[y]+=1
        q=deque()
        for i in range(n):
            if ind[i]==1:
                q.append(i)
        rem=n
        while rem>2:
            s=len(q)
            rem-=s
            for _ in range(s):
                x=q.popleft()
                for nei in g[x]:
                    ind[nei]-=1
                    if ind[nei]==1:
                        q.append(nei)
        return list(q)