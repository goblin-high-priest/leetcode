class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        """
        Recursion
        
        Time Complexity: O(nk)
        Space Complexity: O(nk)
        """

        # n = len(prices)

        # @cache
        # def dfs(i, j, hold):

        #     if j < 0:
        #         return -inf
            
        #     if i < 0:
        #         return -inf if hold else 0
            
        #     if hold:
        #         return max(dfs(i - 1, j, True), dfs(i - 1, j - 1, False) - prices[i])
            
        #     return max(dfs(i - 1, j, True) + prices[i], dfs(i - 1, j, False))
        
        # return dfs(n - 1, k, False)

        """
        Iteration
        
        Time Complexity: O(nk)
        Space Complexity: O(nk)
        """

        # n = len(prices)
        # f = [[[-inf] * 2 for _ in range(k + 2)] for _ in range(n + 1)]

        # for j in range(1, k + 2):
        #     f[0][j][0] = 0
        
        # for i, p in enumerate(prices):
            
        #     for j in range(1, k + 2):
        #         f[i+1][j][0] = max(f[i][j][0], f[i][j][1] + p)
        #         f[i+1][j][1] = max(f[i][j - 1][0] - p, f[i][j][1])

        # return f[-1][-1][0]

        """
        Iteration with Space Optimized
        
        Time Complexity: O(nk)
        Space Complexity: O(k)
        """
        
        f = [[-inf] * 2 for _ in range(k + 2)]

        for j in range(1, k + 2):
            f[j][0] = 0
        
        for p in prices:

            for j in range(k + 1, 0, -1):
                f[j][0] = max(f[j][0], f[j][1] + p)
                f[j][1] = max(f[j-1][0] - p, f[j][1])
            
        return f[-1][0]
