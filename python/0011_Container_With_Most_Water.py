class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        left = 0
        right = len(height) - 1

        while left < right:
            area = min(height[left], height[right]) * (right - left)
            res = max(res, area)

            if height[left] < height[right]:
                # prune
                cur = height[left]
                while height[left] <= cur and left < right:
                    left += 1
            else:
                # prune
                cur = height[right]
                while height[right] <= cur and left < right:
                    right -= 1
        
        return res