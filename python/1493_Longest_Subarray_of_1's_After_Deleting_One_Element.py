class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        res = 0
        cnt0 = cnt1 = 0
        
        left = 0
        for right, x in enumerate(nums):
            
            if x == 0:
                cnt0 += 1
            else:
                cnt1 += 1
            
            while cnt0 > 1:

                if nums[left] == 0: 
                    cnt0 -= 1
                else:
                    cnt1 -= 1
                
                left += 1
            
            res = max(res, cnt1)
        
        return res if cnt0 == 1 else res - 1