class Solution:
    def at_most_k(self, nums: List[int], k: int) -> int:
        cnt = defaultdict(int)
        res = 0

        left = 0
        for right, x in enumerate(nums):
            cnt[x] += 1
            
            while len(cnt) > k:
                left_c = nums[left]
                cnt[left_c] -= 1

                if cnt[left_c] == 0:
                    del cnt[left_c]
                
                left += 1
            
            res += right - left + 1
        
        return res


    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:

        return self.at_most_k(nums, k) - self.at_most_k(nums, k - 1)