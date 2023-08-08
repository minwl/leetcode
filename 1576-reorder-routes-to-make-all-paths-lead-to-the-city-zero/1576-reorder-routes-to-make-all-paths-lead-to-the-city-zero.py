class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:


        adj = dict()
        for link in connections:
            a = link[0]
            b = link[1]
            if a in adj: adj[a].append((b, True))
            else: adj[a] = [(b, True)]
            if b in adj: adj[b].append((a, False))
            else: adj[b] = [(a, False)]
        
        count = 0
        q = [0]
        visited = set()
        while q:
            curr = q.pop()
            visited.add(curr)
            for node, forward in adj[curr]:
                if node not in visited:
                    q.append(node)
                    if forward:
                        count += 1
        return count


        


        


     

