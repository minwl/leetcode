class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        r, c = len(grid), len(grid[0])
        ans = [0 for _ in range(c)]
        for i in range(c):
            self.dfs(grid, 0, i, r,c,ans , i)
        return ans
        
    def dfs(self, grid, x, y, r, c, ans, idx):
        if grid[x][y] == 1:
            if y+1 < c and grid[x][y+1] == 1:
                if x+1 < r:
                    self.dfs(grid, x+1, y+1,r,c,ans, idx)
                elif x == r-1: 
                    ans[idx] = y+1
                    return ans
                else:
                    ans[idx] = -1
                    return ans
            else: 
                ans[idx] = -1
                return ans
        if grid[x][y] == -1:
            if y-1>=0 and grid[x][y-1] == -1 :
                if x+1 < r:
                    self.dfs(grid, x+1, y-1,r,c,ans, idx)
                elif x == r-1 :
                    ans[idx] = y-1
                    return ans
                else:
                    ans[idx] = -1
                    return ans
                
            else: 
                ans[idx] = -1
                return ans