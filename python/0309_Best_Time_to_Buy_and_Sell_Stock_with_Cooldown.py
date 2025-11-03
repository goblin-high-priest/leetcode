class Solution:
    def maxProfit(self, prices: List[int]) -> int:
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
        #         return max(dfs(i - 1, True), dfs(i - 2, False) - prices[i])

        #     return max(dfs(i - 1, True) + prices[i], dfs(i - 1, False))
        
        # return dfs(n - 1, False)

        """
        Iteration
        
        Time Complexity: O(n)
        Space Complexity: O(n)
        """

        # n = len(prices)
        # f = [[0] * 2 for _ in range(n + 2)]
        # f[1][1] = -inf

        # for i, p in enumerate(prices):
        #     f[i+2][0] = max(f[i+1][0], f[i+1][1] + p)
        #     f[i+2][1] = max(f[i][0] - p, f[i+1][1])
        
        # return f[-1][0]

        """
        Iteration with Space Optimized
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        
        pre0, f0, f1 = 0, 0, -inf

        for p in prices:
            pre0, f0, f1 = f0, max(f0, f1 + p), max(pre0 - p, f1) 
        
        return f0