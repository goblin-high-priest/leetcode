class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        pre_sum = 0
        left = 0
        res = 0
        nums.sort()

        for right, x in enumerate(nums):
            
            while right > 0 and x * (right - left) - pre_sum > k:
                pre_sum -= nums[left]
                left += 1

            pre_sum += x
            res = max(res, right - left + 1)
        
        return res
