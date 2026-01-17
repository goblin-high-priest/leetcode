class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = 0

        left = 0
        for right, x in enumerate(nums):
            mn = nums[left]

            while mn * k < x:
                left += 1
                mn = nums[left]
            
            res = max(res, right - left + 1)
        
        return len(nums) - res