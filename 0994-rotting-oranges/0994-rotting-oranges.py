class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        q = deque()
        fresh = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1

        # No fresh oranges
        if fresh == 0:
            return 0

        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        minutes = 0

        while q and fresh > 0:
            size = len(q)

            for _ in range(size):
                x, y = q.popleft()

                for dx, dy in directions:
                    nx, ny = x + dx, y + dy

                    if (0 <= nx < rows and
                        0 <= ny < cols and
                        grid[nx][ny] == 1):

                        grid[nx][ny] = 2
                        fresh -= 1
                        q.append((nx, ny))
            minutes += 1
        return minutes if fresh == 0 else -1
