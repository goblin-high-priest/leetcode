def lower_bound(nums: List[int], target: int) -> int:
    left, right = 0, len(nums)

    while left < right:
        mid = (right - left) // 2 + left

        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid
        
    return left

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = lower_bound(nums, target)

        if left == len(nums) or nums[left] != target:
            return [-1, -1]

        right = lower_bound(nums, target + 1) - 1

        return [left, right]