class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        res = 0
        cnt = defaultdict(int)

        left = 0
        cur = 0
        for x in nums:
            cnt[x] += 1
            cur += x

            while cnt[x] > 1:
                cnt[nums[left]] -= 1
                cur -= nums[left]
                left += 1
            
            res = max(res, cur)
        
        return res