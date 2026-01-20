class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        res = inf
        rem = target % sum(nums)
        tmp = target // sum(nums) * len(nums)
        nums = nums + nums

        left = cur = 0
        for right, x in enumerate(nums):
            cur += x
            
            while cur > rem:
                cur -= nums[left]
                left += 1
            
            if cur == rem:
                res = min(res, right - left + 1)
            
        return res + tmp if res != inf else -1
