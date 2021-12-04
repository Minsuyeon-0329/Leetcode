class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        numRooms=len(rooms)
        visited=set()
        keys=[0]
        while keys:
            curr=keys.pop(-1)
            if curr not in visited:
                visited.add(curr)
                keys.extend(rooms[curr])
        return len(visited)==numRooms