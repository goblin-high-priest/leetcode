MOD = 10 ** 9 + 7
MX = 10 ** 5

pow2 = [1] * MX

for i in range(1, MX):
    pow2[i] = pow2[i-1] * 2 % MOD

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = 0
        l, r = 0, len(nums) - 1

        while l <= r:

            if nums[l] + nums[r] <= target:
                res += pow2[r-l]
                l += 1
            else:
                r -= 1
        
        return res % MOD