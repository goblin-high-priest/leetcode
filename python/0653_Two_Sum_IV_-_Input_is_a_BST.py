# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        s = set()

        def traverse(root):

            if not root:
                return False
            
            if root.val in s:
                return True
            
            s.add(k - root.val)

            return traverse(root.left) or traverse(root.right)
        
        return traverse(root)