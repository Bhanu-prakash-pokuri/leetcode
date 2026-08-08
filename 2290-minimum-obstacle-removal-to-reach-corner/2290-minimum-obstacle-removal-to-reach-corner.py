class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        dist = [[float('inf')] * n for _ in range(m)]
        dist[0][0] = 0

        q = deque([(0, 0)])

        while q:
            r, c = q.popleft()

            if r == m - 1 and c == n - 1:
                return dist[r][c]

            for dr, dc in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                nr, nc = r + dr, c + dc

                if nr < 0 or nr == m or nc < 0 or nc == n:
                    continue

                cost = grid[nr][nc]

                newcost = dist[r][c] + cost

                if newcost < dist[nr][nc]:
                    dist[nr][nc] = newcost

                    if cost == 0:
                        q.appendleft((nr, nc))
                    else:
                        q.append((nr, nc))

        return dist[m - 1][n - 1]