class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = 1_000_000_007
        
        @cache
        def dfs(i):
            
            if i == 0:
                return 1
            elif i < 0:
                return 0
            else:
                return (dfs(i - zero) + dfs(i - one)) % MOD
            
        return (sum([dfs(i) for i in range(low, high + 1)])) % MOD
