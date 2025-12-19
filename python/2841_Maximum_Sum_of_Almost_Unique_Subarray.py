class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        res = 0
        cnt = defaultdict(int)

        cur = 0
        for right, x in enumerate(nums):
            cnt[x] += 1
            left = right - k + 1
            cur += x

            if left < 0: continue

            if len(cnt) >= m: res = max(res, cur)
            
            cnt[nums[left]] -= 1

            if cnt[nums[left]] == 0: del cnt[nums[left]]

            cur -= nums[left]
        
        return res