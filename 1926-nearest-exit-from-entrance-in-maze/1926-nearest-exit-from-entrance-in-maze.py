class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m,n=len(maze),len(maze[0])
        r,c=entrance
        q=deque()
        q.append((r,c,0))
        maze[r][c]='+'
        while q:
            x,y,steps=q.popleft()
            dir=((0,1),(0,-1),(1,0),(-1,0))
            for dr,dc in dir:
                nr,nc=x+dr,y+dc
                if nr<0 or nr==m or nc<0 or nc==n or maze[nr][nc]!='.':
                    continue
                if nr==0 or nr==m-1 or nc==0 or nc==n-1:
                    return steps+1
                maze[nr][nc]='+'
                q.append((nr,nc,steps+1))
        return -1

                