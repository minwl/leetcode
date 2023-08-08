class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [0 for _ in range(n)] 
        total = 0

        def dfs(i, n, isConnected, visited):
            for j in range(n):
                if isConnected[i][j] == 1 and visited[j] == 0:
                    visited[j] = 1
                    dfs(j, n, isConnected, visited)

        for i in range(n):
            if visited[i] == 0:
                dfs(i, n, isConnected, visited)
                total += 1

        return total




