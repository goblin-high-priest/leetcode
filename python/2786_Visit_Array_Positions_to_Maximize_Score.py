class Solution:
    def maxScore(self, nums: List[int], x: int) -> int:
        """
        Recursion
        
        Time Complexity: O(n)
        Space Complexity: O(n)
        """

        # n = len(nums)

        # @cache
        # def dfs(i, parity):
            
        #     if i == n:
        #         return 0

        #     if parity == nums[i] % 2:
        #         return dfs(i + 1, parity) + nums[i]

        #     return max(dfs(i + 1, parity), dfs(i + 1, 1 - parity) + nums[i] - x)

        # return dfs(0, nums[0] % 2)

        n = len(nums)

        @cache
        def dfs(i, parity):
            p = nums[i] % 2

            if i == 0:
                return nums[0] if nums[0] % 2 == parity else nums[0] - x
                
            if p == parity:
                return nums[i] + dfs(i - 1, p)
            
            return max(dfs(i - 1, parity), dfs(i - 1, p) + nums[i] - x)

        return max(dfs(n - 1, 1), dfs(n - 1, 0))

        """
        Iteration
        
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
