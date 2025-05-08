class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = 0
        j = 0
        current_sum = 0
        result = float("inf")

        while j < len(nums):
            current_sum += nums[j]

            while current_sum >= target:
                result = min(result, j - i + 1)
                current_sum -= nums[i]
                i += 1

            j += 1
            
        return result if result != float("inf") else 0