class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        @cache
        def dfs(i, amount):

            if amount < 0:
                return 0

            if i < 0:
                return 1 if amount == 0 else 0
            
            return dfs(i - 1, amount) + dfs(i, amount - coins[i])
        
        return dfs(len(coins) - 1, amount)
