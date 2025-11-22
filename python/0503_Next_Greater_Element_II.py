class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        """
        From right to left
        
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        # n = len(nums)
        # res = [-1] * n
        # stack = []

        # for i in range(2 * n - 1, -1, -1):

        #     v = nums[i % n]
        #     while stack and v >= stack[-1]:
        #         stack.pop()
            
        #     if stack and i < n:
        #         res[i] = stack[-1]
            
        #     stack.append(v)
        
        # return res

        """
        From left to right
        
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        n = len(nums)
        res = [-1] * n
        stack = []

        for i in range(2 * n - 1):
            
            v = nums[i % n]
            while stack and v > nums[stack[-1]]:
                res[stack[-1]] = v
                stack.pop()
            
            if i < n:
                stack.append(i)
            
        return res