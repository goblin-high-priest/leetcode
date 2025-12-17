# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        stack = []

        for x in nums:
            node = TreeNode(x)

            while stack and stack[-1].val < x:
                node.left = stack.pop()
            
            if stack:
                stack[-1].right = node
            
            stack.append(node)

        return stack[0] if stack else None
