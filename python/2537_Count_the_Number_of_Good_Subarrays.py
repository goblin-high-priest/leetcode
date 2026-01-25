class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        res = 0
        cnt = defaultdict(int)

        left = cur_k = 0
        for x in nums:
            cur_k += cnt[x]
            cnt[x] += 1

            while cur_k >= k:
                left_x = nums[left]                
                cnt[left_x] -= 1
                cur_k -= cnt[left_x]
                left += 1
            
            res += left
        
        return res