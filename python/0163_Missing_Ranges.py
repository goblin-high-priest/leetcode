class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        res = []
        nums = [lower-1] + nums + [upper+1]

        for i in range(len(nums) - 1):
            left, right = nums[i], nums[i+1]

            if right - left > 1:
                res.append([left+1, right-1])
            
        return res