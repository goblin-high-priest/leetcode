class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        q = deque()
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited = set()
        m = len(mat)
        n = len(mat[0])
        res = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):

                if mat[i][j] == 0:
                    visited.add((i, j))
                    q.append((i, j))
        
        dist = 1

        while q:
            for _ in range(len(q)):
                i, j = q.popleft()

                for dx, dy in directions:
                    r, c = i + dx, j + dy

                    if 0 <= r < m and 0 <= c < n and (r, c) not in visited:
                        visited.add((r, c))
                        q.append((r, c))
                        res[r][c] = dist
            
            dist += 1
        
        return res
