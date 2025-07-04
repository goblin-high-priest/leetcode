# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode, max_val = -float('inf')) -> int:
        
        if root is None:
            return 0
        
        left = self.goodNodes(root.left, max_val=max(max_val, root.val))
        right = self.goodNodes(root.right, max_val=max(max_val, root.val))

        return left + right + (root.val >= max_val)
