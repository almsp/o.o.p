class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = set()
        keys = set([0])
        while keys:
            room = keys.pop()
            visited.add(room)
            for key in rooms[room]:
                if key not in visited:
                    keys.add(key)
        return len(visited) == n