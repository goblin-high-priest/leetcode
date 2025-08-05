class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        @cache
        def dfs(i, j):

            if i == 0 and j == 0:
                return grid[i][j]
                
            if i < 0 or j < 0:
                return float('inf')

            return grid[i][j] + min(dfs(i - 1, j), dfs(i, j - 1))
        
        return dfs(len(grid) - 1, len(grid[0]) - 1)
