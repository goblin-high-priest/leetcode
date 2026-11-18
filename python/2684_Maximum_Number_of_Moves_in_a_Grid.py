class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        @cache
        def dfs(row, col):
            
            if col == cols - 1:
                return 0
            
            best = 0
            next_col = col + 1

            for next_row in (row - 1, row, row + 1):

                if 0 <= next_row < rows:
                    if grid[next_row][next_col] > grid[row][col]:
                        moves = 1 + dfs(next_row, next_col)
                        best = max(best, moves)
            
            return best
        
        answer = 0
        for row in range(rows):
            answer = max(answer, dfs(row, 0))
        
        return answer
