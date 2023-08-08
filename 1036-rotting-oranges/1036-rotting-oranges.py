class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        m = len(grid[0])
        fresh = 0
        adj = [(0,1), (0, -1), (1, 0), (-1,0)]
        q = []

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    q.append((i,j))
          
        minute = 0

        while q and fresh > 0:
            minute += 1
            for _ in range(len(q)):
                x,y = q.pop(0)
                for dx, dy in adj:
                    rx = x + dx
                    ry = y + dy
                    if rx > n-1 or rx < 0 or ry > m-1 or ry < 0:
                        continue
                    
                    if grid[rx][ry] == 1:   
                        grid[rx][ry] = 2
                        fresh -= 1
                        q.append((rx, ry))
        
        if fresh == 0:
            return minute
        else:
            return -1








