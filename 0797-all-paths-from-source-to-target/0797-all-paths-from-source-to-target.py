class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        d=defaultdict(list)
        n=len(graph)
        for i in range(n):
            d[i].append(graph[i])
        stack=[(0,[0])]
        res=[]
        while stack:
            node,path=stack.pop()
            if node==n-1:
                res.append(path)
            for nei in graph[node]:
                stack.append((nei,path+[nei]))
        return res