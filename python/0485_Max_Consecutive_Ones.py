class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        maxConsecutiveOnes = 0

        cur = 0
        for num in nums:

            if num == 1:
                cur += 1
            else:
                cur = 0
            
            maxConsecutiveOnes = max(maxConsecutiveOnes, cur)
        
        return maxConsecutiveOnes
