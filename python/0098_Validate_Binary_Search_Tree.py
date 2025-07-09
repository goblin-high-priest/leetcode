# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode], l_max=-float('inf'), r_min=float('inf')) -> bool:
        
        if root is None:
            return True
        
        return l_max < root.val < r_min and self.isValidBST(root.left, l_max, root.val) and self.isValidBST(root.right, root.val, r_min)
        