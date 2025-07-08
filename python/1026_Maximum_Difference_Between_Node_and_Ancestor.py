# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        result = 0

        def dfs(root, min_val, max_val):

            if root is None:
                return

            min_val = min(min_val, root.val)
            max_val = max(max_val, root.val)

            nonlocal result 
            result = max(result, max_val - min_val)

            dfs(root.left, min_val, max_val)
            dfs(root.right, min_val, max_val)
        
        dfs(root, float('inf'), -float('inf'))

        return result

