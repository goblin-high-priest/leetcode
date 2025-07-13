# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        if not preorder:
            return None

        if len(preorder) == 1:  
            return TreeNode(preorder[0])

        left_size = postorder.index(preorder[1]) + 1
        left = self.constructFromPrePost(preorder[1:left_size+1], postorder[:left_size])
        right = self.constructFromPrePost(preorder[left_size+1:], postorder[left_size:-1])

        return TreeNode(preorder[0], left, right)