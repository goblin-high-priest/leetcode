# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if root is None:
            return []
        
        q = deque([root])
        result = []
        reverse = False

        while q:
            vals = []

            for _ in range(len(q)):
                node = q.popleft()
                vals.append(node.val)

                if node.left:
                    q.append(node.left)
                
                if node.right:
                    q.append(node.right)

            if reverse:
                vals = vals[::-1]
                
            result.append(vals)
            reverse = not reverse
        
        return result
        