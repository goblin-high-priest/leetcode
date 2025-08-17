# class Solution:
#     def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
#         MOD = 1_000_000_007
        
#         @cache
#         def dfs(i):
            
#             if i == 0:
#                 return 1
#             elif i < 0:
#                 return 0
#             else:
#                 return (dfs(i - zero) + dfs(i - one)) % MOD
            
#         return (sum([dfs(i) for i in range(low, high + 1)])) % MOD

class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = 1_000_000_007
        f = [1] + [0] * high

        for i in range(1, high + 1):

            if i >= zero:
                f[i] = f[i-zero]
            
            if i >= one:
                f[i] = (f[i] + f[i-one]) % MOD
            
        return sum(f[low:]) % MOD
