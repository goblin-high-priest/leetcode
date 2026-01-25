class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        res = 0
        k = len(set(nums))
        cnt = defaultdict(int)

        left = 0
        for x in nums:
            cnt[x] += 1

            while len(cnt) == k:
                left_x = nums[left]
                cnt[left_x] -= 1
                left += 1

                if cnt[left_x] == 0: del cnt[left_x]

            res += left
        
        return res