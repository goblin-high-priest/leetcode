# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        root.val = 0
        q = [root]

        while q:
            tmp = q
            q = []
            next_level_sum = 0

            for node in tmp:
                
                if node.left:
                    q.append(node.left)
                    next_level_sum += node.left.val
                
                if node.right:
                    q.append(node.right)
                    next_level_sum += node.right.val

            for node in tmp:

                children_sum = (node.left.val if node.left else 0) + (node.right.val if node.right else 0)

                if node.left:
                    node.left.val = next_level_sum - children_sum
                
                if node.right:
                    node.right.val = next_level_sum - children_sum
                
        return root