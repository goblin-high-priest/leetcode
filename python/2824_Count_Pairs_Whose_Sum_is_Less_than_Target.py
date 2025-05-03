class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        i = 0
        j = len(nums) - 1
        res = 0
        while j > 0:
            if nums[i] + nums[j] < target and i < j:
                i += 1
                res += 1
            else:
                j -= 1
                i = 0
        return res