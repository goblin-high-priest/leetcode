class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        """
        Recursion
        
        Time Complexity: O(n ** 3)
        Space Complexity: O(n ** 2)
        """

        # n = len(values)

        # @cache
        # def dfs(i, j):

        #     if i + 1 == j:
        #         return 0
            
        #     return min(dfs(i, k) + dfs(k, j) + values[i] * values[k] * values[j] for k in range(i + 1, j))
        
        # return dfs(0, n - 1)

        """
        Iteration
        
        Time Complexity: O(n ** 3)
        Space Complexity: O(n ** 2)
        """

        n = len(values)
        f = [[0] * n for _ in range(n)]

        for i in range(n - 3, -1, -1):

            for j in range(i + 2, n):
                f[i][j] = min(f[i][k] + f[k][j] + values[i] * values[j] * values[k] for k in range(i + 1, j))
            
        return f[0][-1]
