class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left = 0
        res = 0
        prod = 1

        if k <= 1:
            return 0

        for right in range(len(nums)):
            prod *= nums[right]

            while prod >= k:
                prod //= nums[left]
                left += 1
            
            res += right - left + 1
        
        return res