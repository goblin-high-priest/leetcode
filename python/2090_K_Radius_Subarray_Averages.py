class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        res = [-1] * len(nums)

        cur = 0
        for right, x in enumerate(nums):
            cur += x

            if right < 2 * k:
                continue
            
            res[right-k] = cur // (2 * k + 1)
            cur -= nums[right-2*k]

        return res