class Solution:
    def trap(self, height: List[int]) -> int:
        length = len(height)
        sum = 0

        prefix_max = [0] * length
        prefix_max[0] = height[0]
        for i in range(1, length):
            prefix_max[i] = max(prefix_max[i-1], height[i])
        
        suffix_max = [0] * length
        suffix_max[length-1] = height[length-1]
        for i in range(length - 2, -1, -1):
            suffix_max[i] = max(height[i], suffix_max[i+1])
        
        for pre, suf, height in zip(prefix_max, suffix_max, height):
            sum += min(pre, suf) - height
        
        return sum