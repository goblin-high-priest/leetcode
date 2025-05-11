class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        left = 0
        res = 0
        cur_sum = 0

        for right, x in enumerate(nums):
            cur_sum += x

            while cur_sum * (right - left + 1) >= k:
                cur_sum -= nums[left]
                left += 1
                
            res += right - left + 1

        return res