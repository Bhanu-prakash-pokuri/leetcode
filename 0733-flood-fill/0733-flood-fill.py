class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        #using dfs
        # old = image[sr][sc]
        # if old == color:
        #     return image
        # m = len(image)
        # n = len(image[0])
        # def dfs(i, j):
        #     if i < 0 or i >= m or j < 0 or j >= n or image[i][j] != old:
        #         return
        #     image[i][j] = color
        #     dfs(i + 1, j)
        #     dfs(i - 1, j)
        #     dfs(i, j + 1)
        #     dfs(i, j - 1)
        # dfs(sr, sc)
        # return image

        # using bfs
        old, m, n = image[sr][sc], len(image), len(image[0])
        if old != color: 
            q = deque([(sr, sc)])
            while q:
                i, j = q.popleft()
                image[i][j] = color
                for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                    if 0 <= x < m and 0 <= y < n and image[x][y] == old: 
                        q.append((x, y))
        return image
