# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node: Optional[TreeNode]) -> Tuple[int, int, int]:
            
            if node is None:
                return inf, 0, 0
            
            l_choose, l_by_parent, l_by_children = dfs(node.left)
            r_choose, r_by_parent, r_by_children = dfs(node.right)
            choose = min(l_choose, l_by_parent) + min(r_choose, r_by_parent) + 1
            by_parent = min(l_choose, l_by_children) + min(r_choose, r_by_children)
            by_children = min(l_choose + r_by_children, l_by_children + r_choose, l_choose + r_choose)
            
            return choose, by_parent, by_children
        
        choose, _, by_children = dfs(root)

        return min(choose, by_children)