class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)

        if s % 2 == 1:
            return False
        
        target = s // 2

        @cache
        def dfs(i, s):

            if i < 0:
                return True if s == target else False
            
            return dfs(i - 1, s) or dfs(i - 1, s - nums[i])
        
        return dfs(len(nums) - 1, s)