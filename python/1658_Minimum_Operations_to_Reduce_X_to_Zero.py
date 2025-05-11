class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        res = -1
        left = 0
        cur_sum = 0
        target = sum(nums) - x

        if target < 0:
            return -1
        
        for right, v in enumerate(nums):
            cur_sum += v

            while cur_sum > target:
                cur_sum -= nums[left]
                left += 1
            
            if cur_sum == target:
                res = max(res, right - left + 1)
            
        return -1 if res < 0 else len(nums) - res