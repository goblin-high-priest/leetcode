# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         n = len(nums)
        
#         @cache
#         def dfs(i):

#             if i < 0:
#                 return 0
            
#             return max(dfs(i - 1), dfs(i - 2) + nums[i])
        
#         return dfs(n - 1)

# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         f = [0] * (len(nums) + 2)

#         for i, x in enumerate(nums):
#             f[i+2] = max(f[i+1], f[i] + x)
        
#         return f[-1]

class Solution:
    def rob(self, nums: List[int]) -> int:
        f0 = f1 = 0

        for i, x in enumerate(nums):
            f0, f1 = f1, max(f0 + x, f1)
        
        return f1