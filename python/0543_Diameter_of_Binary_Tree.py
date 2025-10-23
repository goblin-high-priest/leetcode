# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def longest_path(root):
            nonlocal res

            if root is None:
                return -1
            
            left_longest_path = 1 + longest_path(root.left) 
            right_longest_path = 1 + longest_path(root.right)
            res = max(res, left_longest_path + right_longest_path)
            
            return max(left_longest_path, right_longest_path)
        
        longest_path(root)

        return res
