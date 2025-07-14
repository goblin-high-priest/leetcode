# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        result = []
        to_delete = set(to_delete)

        def dfs(root):
            
            if root is None:
                return None
            
            root.left = dfs(root.left)
            root.right = dfs(root.right)

            if root.val in to_delete:
                if root.left:
                    result.append(root.left)
                if root.right:
                    result.append(root.right)
                return None
            else:
                return root

        if dfs(root):
            result.append(root)
        
        return result