class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        """
        Recursion
        
        Time Complexity: O(m ** 3)
        Space Complexity: O(m ** 2)
        """

        # cuts.sort()
        # cuts = [0] + cuts + [n]

        # @cache
        # def dfs(i, j):
            
        #     if i + 1 == j:
        #         return 0
            
        #     return min(dfs(i, k) + dfs(k, j) for k in range(i + 1, j)) + cuts[j] - cuts[i]
        
        # return dfs(0, len(cuts) - 1)

        """
        Iteration
        
        Time Complexity: O(m ** 3)
        Space Complexity: O(m ** 2)
        """

        cuts.sort()
        cuts = [0] + cuts + [n]

        m = len(cuts)
        f = [[0] * m for _ in range(m)]

        for i in range(m - 3, -1, -1):

            for j in range(i + 2, m):
                f[i][j] = min(f[i][k] + f[k][j] for k in range(i + 1, j)) + cuts[j] - cuts[i]
            
        return f[0][-1]
