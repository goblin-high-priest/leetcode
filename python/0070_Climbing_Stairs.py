# class Solution:
#     def climbStairs(self, n: int) -> int:
#         cache = [-1] * (n + 1)

#         def dfs(i):

#             if i == 0 or i == 1:
#                 return 1
            
#             if cache[i] != -1:
#                 return cache[i]

#             res = dfs(i - 1) + dfs(i - 2)
#             cache[i] = res

#             return res

#         return dfs(n)

# class Solution:
#     def climbStairs(self, n: int) -> int:
#         f = [0] * (n + 1)
#         f[0] = f[1] = 1

#         for i in range(2, n + 1):
#             f[i] = f[i-1] + f[i-2]
        
#         return f[-1]

class Solution:
    def climbStairs(self, n: int) -> int:
        f0 = f1 = 1

        for i in range(2, n + 1):
            f0, f1 = f1, f0 + f1
        
        return f1