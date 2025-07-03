# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode], x=0) -> int:
        
        if root is None:
            return 0
        
        if root.left is root.right:
            return 10 * x + root.val
        
        x = 10 * x + root.val

        return self.sumNumbers(root.left, x) + self.sumNumbers(root.right, x)