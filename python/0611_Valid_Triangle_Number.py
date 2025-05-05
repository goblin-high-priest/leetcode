"""
This algorithm is adapted from a solution to the LeetCode (China) problem
"Valid Triangle Number", which can be found at the following URL:
https://leetcode.cn/problems/valid-triangle-number/solutions/2432875/zhuan-huan-cheng-abcyong-xiang-xiang-shu-1ex3/
"""
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        for c in range(len(nums) - 1, 1, -1):
            # prune
            if nums[0] + nums[1] > nums[c]:
                ans += (c+1)*c*(c-1) // 6
                return ans
            # prune
            if nums[c-2] + nums[c-1] <= nums[c]:
                continue
            a = 0
            b = c - 1
            while a < b:
                if nums[a] + nums[b] > nums[c]:
                    ans += b - a
                    b -= 1
                else:
                    a += 1
        return ans
