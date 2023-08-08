class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = dict()
        for i in range(len(rooms)):
            visited[i] = False

        def dfs(rooms, room_num, visited):
            if visited[room_num]:
                return True
            else:
                visited[room_num] = True
                new_keys = rooms[room_num]
                for new_key in new_keys:
                    dfs(rooms, new_key, visited)

        

        dfs(rooms, 0, visited)

        for check in visited.values():
            if not check:
                return False
        
        return True


