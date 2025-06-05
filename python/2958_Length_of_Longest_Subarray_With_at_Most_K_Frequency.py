class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        left = 0
        cnt = Counter()
        res = 0

        for right in range(0, len(nums)):
            cnt[nums[right]] += 1

            while cnt[nums[right]] > k:
                cnt[nums[left]] -= 1
                left += 1
            
            res = max(res, right - left + 1)
        
        return res