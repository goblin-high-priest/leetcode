class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        @cache
        def dfs(i):

            if i == 0:
                return 1
            elif i < 0:
                return 0
            
            return sum(dfs(i - step) for step in nums)

        return dfs(target)
