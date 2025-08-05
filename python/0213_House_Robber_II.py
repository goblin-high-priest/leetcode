class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        @cache
        def dfs(i, flag):

            if flag:
                
                if i < 0:
                    return 0
            else:

                if i < 1:
                    return 0
                
            return max(nums[i] + dfs(i - 2, flag), dfs(i - 1, flag))
        
        if n < 2:
            return dfs(n - 1, True)

        return max(dfs(n - 1, False), dfs(n - 2, True))
