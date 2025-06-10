class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        res = 0
        count = 0
        left = 0

        for right in range(len(nums)):

            if nums[right] == 0:
                
                if count < k:
                    count += 1
                else:
                    while nums[left] != 0:
                        left += 1
                    left += 1
                
            res = max(res, right - left + 1)
        
        return res
