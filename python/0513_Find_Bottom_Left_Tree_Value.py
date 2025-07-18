# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        max_depth = 0
        result = None

        def dfs(root, depth):
            nonlocal max_depth, result

            if root is None:
                return
            
            if depth > max_depth:
                max_depth = depth
                result = root.val

            left = dfs(root.left, depth + 1)
            right = dfs(root.right, depth + 1)

        dfs(root, 1)

        return result