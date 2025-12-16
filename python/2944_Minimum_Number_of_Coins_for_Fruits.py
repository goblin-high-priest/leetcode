class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        """
        Recursion
        
        Time Complexity: O(n ** 2)
        Space Complexity: O(n)
        """
        # n = len(prices)

        # @cache
        # def dfs(i: int) -> int:

        #     if i * 2 >= n:
        #         return prices[i-1]
            
        #     return min(dfs(j) for j in range(i + 1, 2 * i + 2)) + prices[i-1]
        
        # return dfs(1)

        """
        Iteration
        
        Time Complexity: O(n ** 2)
        Space Complexity: O(1)
        """
        # n = len(prices)

        # for i in range((n + 1) // 2 - 1, 0, -1):
        #     prices[i-1] += min(prices[i: 2*i+1])
        
        # return prices[0]

        """
        Optimize the Iteration Using a Monotonic Queue
        
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        n = len(prices)
        q = deque([(n + 1, 0)]) # sentinel

        for i in range(n, 0, -1):

            while q[0][0] > 2 * i + 1:
                q.popleft()
            
            f = prices[i-1] + q[0][1]

            while f <= q[-1][1]:
                q.pop()
            
            q.append((i, f))
        
        return q[-1][1]