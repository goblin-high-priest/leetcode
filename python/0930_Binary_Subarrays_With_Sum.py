class Solution:
    def less_than_k(self, nums: List[int], k: int) -> int:
        
        if k == 0: return 0

        res = 0

        left = cur_sum = 0
        for right, x in enumerate(nums):
            cur_sum += x

            while cur_sum == k:
                left_x = nums[left]
                cur_sum -= left_x
                left += 1
            
            res += right - left + 1
        
        return res


    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        return self.less_than_k(nums, goal + 1) - self.less_than_k(nums, goal)