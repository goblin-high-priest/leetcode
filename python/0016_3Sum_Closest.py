from math import *
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        gap = inf
        res = inf
        nums.sort()
        length = len(nums)
        for i in range(length - 2):
            # prune
            if i > 0 and nums[i] == nums[i-1]:
                continue

            # prune
            temp = nums[i] + nums[i+1] + nums[i+2]
            if temp > target:
                if abs(temp - target) < gap:
                    gap = abs(temp - target)
                    res = temp       
                continue   

            # prune
            temp = nums[i] + nums[length-2] + nums[length-1]
            if temp < target:
                if abs(temp - target) < gap:
                    gap = abs(temp - target)
                    res = temp       
                continue               


            left = i + 1
            right = length - 1
            while left < right:
                temp = nums[i] + nums[left] + nums[right]

                if abs(temp - target) < gap:
                    gap = abs(temp - target)
                    res = temp
                if temp - target < 0:
                    left += 1
                else:
                    right -= 1
        return res

             