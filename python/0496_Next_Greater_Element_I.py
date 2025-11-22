class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        From right to left

        Time Complexity: O(n + m) where n = len(nums1) and m = len(nums2)
        Space Complexity: O(n + m)
        """
        # idx = {x: i for i, x in enumerate(nums1)}
        # res = [-1] * len(nums1)
        # stack = []

        # for x in reversed(nums2):
            
        #     while stack and x >= stack[-1]:
        #         stack.pop()
            
        #     if stack and x in idx:
        #         res[idx[x]] = stack[-1]
            
        #     stack.append(x)
        
        # return res

        """
        From left to right

        Time Complexity: O(n + m) where n = len(nums1) and m = len(nums2)
        Space Complexity: O(n)
        """
        idx = {x: i for i, x in enumerate(nums1)}
        res = [-1] * len(nums1)
        stack = []

        for x in nums2:

            while stack and x >= stack[-1]:
                res[idx[stack[-1]]] = x
                stack.pop()
            
            if x in idx:
                stack.append(x)
        
        return res