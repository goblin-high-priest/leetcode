class Solution:
    def perfectPairs(self, nums: List[int]) -> int:
        # b - a <= a && a + b >= b
        nums.sort(key=abs)
        res = 0
        left = 0

        for right, v in enumerate(nums):

            while abs(nums[left]) * 2 < abs(v):
                left += 1
            
            res += right - left
        
        return res