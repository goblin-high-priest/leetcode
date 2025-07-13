# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        if not postorder:
            return None
        
        left_size = inorder.index(postorder[-1])
        left = self.buildTree(inorder[:left_size], postorder[:left_size])
        right = self.buildTree(inorder[left_size+1:], postorder[left_size:-1])

        return TreeNode(postorder[-1], left, right)