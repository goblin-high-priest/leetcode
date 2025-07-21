# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if root is None:
            return []

        q = [root]
        reverse = False

        while q:

            if reverse:

                for i in range(len(q) // 2):
                    q[i].val, q[len(q) - i - 1].val = q[len(q) - i - 1].val, q[i].val
                
            tmp = q
            q = []
            
            for node in tmp:
                
                if node.left:
                    q.append(node.left)
                
                if node.right:
                    q.append(node.right)
            
            reverse = not reverse
                
        return root
