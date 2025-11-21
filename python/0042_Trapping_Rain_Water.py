class Solution:
    def trap(self, height: List[int]) -> int:
        """
        Prefix–Suffix Decomposition

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        # length = len(height)
        # sum = 0

        # prefix_max = [0] * length
        # prefix_max[0] = height[0]
        # for i in range(1, length):
        #     prefix_max[i] = max(prefix_max[i-1], height[i])
        
        # suffix_max = [0] * length
        # suffix_max[length-1] = height[length-1]
        # for i in range(length - 2, -1, -1):
        #     suffix_max[i] = max(height[i], suffix_max[i+1])
        
        # for pre, suf, height in zip(prefix_max, suffix_max, height):
        #     sum += min(pre, suf) - height
        
        # return sum
        
        """
        Monotonic Stack
        
        Time Complexity: O(n)
        Space Complexity: O(min(n,U)), where U = max(height) − min(height) + 1
        """
        res = 0
        stack = []

        for i, h in enumerate(height):

            while stack and h > height[stack[-1]]:
                bottom_h = height[stack.pop()]

                if not stack:
                    break
                
                left = stack[-1]
                h_diff = min(height[left], h) - bottom_h
                length = i - left - 1
                res += h_diff * length

            stack.append(i)
        
        return res