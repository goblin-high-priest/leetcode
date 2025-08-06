class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        @cache
        def dfs(amount, i):

            if i == 0:
                return 0 if amount == 0 else inf
            
            if amount < 0:
                return inf

            return min(dfs(amount - coins[i-1], i) + 1, dfs(amount, i - 1))
        
        return dfs(amount, len(coins)) if dfs(amount, len(coins)) != inf else -1