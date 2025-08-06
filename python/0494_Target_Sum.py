class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # postive_sum = p
        # negative_absolute_sum = s - p
        # target = p - s + p
        # p = (target + s) / 2
        p = target + sum(nums)

        if p < 0 or p % 2 != 0:
            return 0
        
        p = p / 2

        @cache
        def dfs(p, i):
            
            if i == 0:
                return 1 if p == 0 else 0
            
            return dfs(p, i - 1) + dfs(p - nums[i-1], i - 1)

        return dfs(p, len(nums))