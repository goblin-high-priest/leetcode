# class Solution:
#     def minCostClimbingStairs(self, cost: List[int]) -> int:
#         n = len(cost)

#         @cache
#         def dfs(i):

#             if i <= 1:
#                 return 0
            
#             return min(cost[i-1] + dfs(i - 1), cost[i-2] + dfs(i - 2))

#         return dfs(n)

# class Solution:
#     def minCostClimbingStairs(self, cost: List[int]) -> int:
#         f = [0] * (len(cost) + 1)
        
#         for i in range(2, len(cost) + 1):
#             f[i] = min(f[i-1] + cost[i-1], f[i-2] + cost[i-2])
        
#         return f[-1]

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        f0 = f1 = 0

        for i in range(2, len(cost) + 1):
            f0, f1 = f1, min(f0 + cost[i - 2], f1 + cost[i-1])
        
        return f1