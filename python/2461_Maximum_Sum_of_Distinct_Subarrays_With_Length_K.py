class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        cnt = defaultdict(int)
        res = 0

        cur = 0
        for right, x in enumerate(nums):
            cur += x
            cnt[x] += 1

            left = right - k + 1

            if left < 0: continue

            if len(cnt) == k: res = max(res, cur)

            cnt[nums[left]] -= 1
            cur -= nums[left]

            if cnt[nums[left]] == 0: del cnt[nums[left]]
        
        return res

