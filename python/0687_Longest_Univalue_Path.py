# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(root):

            if root is None:
                return -1
            
            nonlocal res

            left_len = 1 + dfs(root.left) 
            right_len = 1 + dfs(root.right) 

            if root.left and root.val != root.left.val:
                left_len = 0
            
            if root.right and root.val != root.right.val:
                right_len = 0

            res = max(res, left_len + right_len)
            max_len = max(left_len, right_len)

            return max_len
        
        dfs(root)

        return res