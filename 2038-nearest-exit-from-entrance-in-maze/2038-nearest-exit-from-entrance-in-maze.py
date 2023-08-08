class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        r = len(maze)
        c = len(maze[0])
        sx = entrance[0]
        sy = entrance[1]
        exit = []

        for i in range(r):
            for j in range(c):
                if i == 0 or i == r-1 or j == 0 or j == c-1:
                    if maze[i][j] == ".":
                        exit.append((i,j))
        if (sx, sy) in exit : exit.remove((sx, sy))
        q = [(sx, sy,0)]
        
        visited = set()

        adj = [(1,0), (-1,0), (0,1), (0, -1)]

        while q :
            
            x,y,count = q.pop(0)
            if (x,y) in visited:
                continue

            if (x,y) in exit:
                
                return count

            visited.add((x,y))
            for dx, dy in adj:
                nx = x + dx
                ny = y + dy
                if nx >= 0 and nx < r and ny >=0 and ny < c and maze[nx][ny] == '.':
                        q.append((nx, ny,count+1))
                        

                
        return -1
                


