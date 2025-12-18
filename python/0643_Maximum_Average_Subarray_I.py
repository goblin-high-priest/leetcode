class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        res = -inf
        left = right = 0

        cur = 0
        for right in range(len(nums)):
            cur += nums[right]
            left = right - k + 1

            if left < 0:
                continue
            
            res = max(res, cur / k)
            cur -= nums[left]
        
        return res
