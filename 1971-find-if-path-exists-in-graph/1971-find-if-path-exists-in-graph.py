class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        # using dfs
        # g=collections.defaultdict(list)
        # for u,v in edges:
        #     g[u].append(v)
        #     g[v].append(u)
        # def dfs(node,visited):
        #     if node==destination:
        #         return True
        #     visited.add(node)
        #     for n in g[node]:
        #         if n not in visited:
        #             if dfs(n,visited):
        #                 return True
        #     return False
        # visited=set()
        # return dfs(source,visited)

        #using bfs
        g=collections.defaultdict(list)
        for u,v in edges:
            g[u].append(v)
            g[v].append(u)
        queue=deque([source])
        visited=set([source])
        while queue:
            node=queue.popleft()
            if node==destination:
                return True
            for n in g[node]:
                if n not in visited:
                    visited.add(n)
                    queue.append(n)
        return False
       
