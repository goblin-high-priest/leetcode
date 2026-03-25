class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        i = 0
        res = []

        for j, x in enumerate(nums):

            if x == key:
                i = max(i, j - k)

                while i < len(nums) and i <= j + k:
                    res.append(i)
                    i += 1
            
        return res