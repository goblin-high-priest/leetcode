class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        """
        Recursion
        
        Time Complexity: O(n)
        Space Complexity: O(n)
        """

        # n = len(prices)

        # @cache
        # def dfs(i, hold):

        #     if i < 0:
        #         return -inf if hold else 0
            
        #     if hold:
        #         return max(dfs(i - 1, True), dfs(i - 1, False) - prices[i])
            
        #     return max(dfs(i - 1, True) + prices[i] - fee, dfs(i - 1, False))
        
        # return dfs(n - 1, 0)

        """
        Iteration
        
        Time Complexity: O(n)
        Space Complexity: O(n)
        """

        # n = len(prices)
        # f = [[0] * 2 for _ in range(n + 1)]
        # f[0][1] = -inf

        # for i, p in enumerate(prices):
        #     f[i+1][0] = max(f[i][0], f[i][1] + p - fee)
        #     f[i+1][1] = max(f[i][0] - p, f[i][1])
        
        # return f[-1][0]

        """
        Iteration with Space Optimized
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """

        n = len(prices)
        f0, f1 = 0, -inf

        for i, p in enumerate(prices):
            f0, f1 = max(f0, f1 + p - fee), max(f0 - p, f1)
        
        return f0