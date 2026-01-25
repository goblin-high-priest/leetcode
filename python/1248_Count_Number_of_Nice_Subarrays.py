class Solution:
    def at_most_k(self, nums: List[int], k: int) -> int:
        res = 0
        cnt = 0

        left = 0
        for right, x in enumerate(nums):
            cnt += x % 2 

            while cnt > k:
                left_x = nums[left]
                cnt -= left_x % 2
                left += 1
            
            res += right - left + 1
        
        return res

    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        return self.at_most_k(nums, k) - self.at_most_k(nums, k - 1)