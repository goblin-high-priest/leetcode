class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        m, n = len(image), len(image[0])
        source_color = image[sr][sc]
        image[sr][sc] = color
        q = deque()
        q.append((sr, sc))
        visited = set()
        visited.add((sr, sc))
        
        while q:

            for _ in range(len(q)):
                row, col = q.popleft()

                for dr, dc in directions:
                    r, c = row + dr, col + dc

                    if 0 <= r < m and 0 <= c < n and (r, c) not in visited and image[r][c] == source_color:
                        visited.add((r, c))
                        q.append((r, c))
                        image[r][c] = color
        
        return image
