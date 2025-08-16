# class Solution:
#     def combinationSum4(self, nums: List[int], target: int) -> int:

#         @cache
#         def dfs(i):

#             if i == 0:
#                 return 1
#             elif i < 0:
#                 return 0
            
#             return sum(dfs(i - step) for step in nums)

#         return dfs(target)

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        f = [1] + [0] * target

        for i in range(1, target + 1):
            f[i] = sum(f[i - step] for step in nums if step <= i)
        
        return f[-1]
