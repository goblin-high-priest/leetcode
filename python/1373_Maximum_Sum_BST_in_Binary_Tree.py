# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        result = 0

        def dfs(root):

            if root is None:
                return inf, -inf, 0
            
            l_min, l_max, l_sum = dfs(root.left)
            r_min, r_max, r_sum = dfs(root.right)

            if root.val <= l_max or root.val >= r_min:
                return -inf, inf, 0
            
            nonlocal result
            
            if l_sum + r_sum + root.val > result:
                result = l_sum + r_sum + root.val

            return min(l_min, root.val), max(r_max, root.val), l_sum + r_sum + root.val

        dfs(root)

        return result