class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        
        @cache
        def dfs(i, target):

            if i < 0:
                return 0 if target == 0 else -inf
            
            if nums[i] > target:
                return dfs(i - 1, target)

            return max(dfs(i - 1, target), 1 + dfs(i - 1, target - nums[i]))
        
        result = dfs(len(nums) - 1, target)

        dfs.cache_clear()

        return result if result != -inf else -1 
