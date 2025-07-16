# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        max_depth = -1
        result = None

        def dfs(root, depth):
            nonlocal max_depth, result

            if root is None:
                max_depth = max(max_depth, depth)
                return depth
            
            left_max_depth = dfs(root.left, depth + 1)
            right_max_depth = dfs(root.right, depth + 1)

            if left_max_depth == right_max_depth == max_depth:
                result = root
            
            return max(left_max_depth, right_max_depth)
        
        dfs(root, 0)

        return result