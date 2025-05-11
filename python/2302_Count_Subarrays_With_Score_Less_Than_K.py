class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        left = 0
        res = 0
        tmp = 0

        for right, x in enumerate(nums):
            tmp += x

            while tmp * (right - left + 1) >= k:
                tmp -= nums[left]
                left += 1
                
            res += right - left + 1

        return res