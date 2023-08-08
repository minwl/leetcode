class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        #make n by n distance matrix 
        cost = [[float('inf') for _ in range(n)]for _ in range(n)]
        for i in range(n):
            cost[i][i] = 0

        for edge in edges:
            from_= edge[0]
            to = edge[1]
            p = edge[2]
            cost[from_][to] = p
            cost[to][from_] = p

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    cost[i][j] = min(cost[i][j], cost[i][k]+cost[k][j])

        minvisit= float('inf')
        node = 0
        for i in range(n):
            visit = 0
            for j in range(n):
                if cost[i][j] <= distanceThreshold:
                    visit += 1
            if visit <= minvisit:
                minvisit = visit
                node = i
        return node


            