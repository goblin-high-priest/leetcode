class Solution:
    def numDistinctIslands(self, grid: list[list[int]]) -> int:
        
        if not grid or not grid[0]:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visited, shapes = set(), set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def get_shape(start_row, start_col):
            shape = []

            def dfs(row, col):
                visited.add((row, col))

                shape.append((row - start_row, col - start_col))

                for dr, dc in directions:
                    nr, nc = row + dr, col + dc

                    if 0 <= nr < rows and 0 <= nc < cols:
                        if grid[nr][nc] == 1 and (nr, nc) not in visited:
                            dfs(nr, nc)
                    
            dfs(start_row, start_col)
            return tuple(shape)
        
        for row in range(rows):
            for col in range(cols):

                if grid[row][col] == 1 and (row, col) not in visited:
                    shapes.add(get_shape(row, col))
        
        return len(shapes)

