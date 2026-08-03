class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        g=collections.defaultdict(list)
        for u,v in edges:
            g[u].append(v)
            g[v].append(u)
        def dfs(node,visited):
            if node==destination:
                return True
            visited.add(node)
            for n in g[node]:
                if n not in visited:
                    if dfs(n,visited):
                        return True
            return False
        visited=set()
        return dfs(source,visited)