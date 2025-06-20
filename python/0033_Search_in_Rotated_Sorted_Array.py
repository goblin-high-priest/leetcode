class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def is_on_right(mid):

            if nums[mid] > nums[-1]:
                if target > nums[mid] or target < nums[-1]:
                    return True
            else:
                if target > nums[mid] and target < nums[-1]:
                    return True
        
        if target == nums[-1]:
            return len(nums) - 1
            
        left, right = 0, len(nums)

        while left < right:
            mid = (left + right) // 2

            if is_on_right(mid):
                left = mid + 1
            else:
                right = mid
        
        return left if nums[left] == target else -1