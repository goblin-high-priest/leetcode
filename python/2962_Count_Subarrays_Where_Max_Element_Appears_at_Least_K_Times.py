class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        maximum = max(nums)
        left = 0
        count = 0
        res = 0

        for right, x in enumerate(nums):
            
            if x == maximum:

                if count + 1 < k:
                    count += 1
                else:
                    while nums[left] < maximum:
                        left += 1
                    left += 1
            
            res += left
            
        return res
