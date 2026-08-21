class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        visited = set()
        q = deque()
        ROWS, COLS = len(rooms), len(rooms[0])

        def addRoom(r, c):

            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                
                if r + dr >= 0 and r + dr < ROWS and c + dc >= 0 and c + dc < COLS and (r + dr, c + dc) not in visited and rooms[r + dr][c + dc] == 2147483647:
                    q.append((r + dr, c + dc))
                    visited.add((r + dr, c + dc))

        for r in range(ROWS):
            for c in range(COLS):

                if rooms[r][c] == 0:
                    q.append((r, c))
                    visited.add((r, c))
        
        dist = 0
        while q:
            
            for _ in range(len(q)):
                r, c = q.popleft()
                rooms[r][c] = dist
                addRoom(r, c)
            
            dist += 1
