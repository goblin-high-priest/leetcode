# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        groups = defaultdict(list)

        def dfs(root, row=0, col=0):

            if root is None:
                return 

            groups[col].append([row, root.val])

            dfs(root.left, row + 1, col - 1)
            dfs(root.right, row + 1, col + 1)
        
        dfs(root)
        groups = dict(sorted(groups.items()))
        result = []

        for col in groups.keys():
            groups[col].sort(key=lambda x : (x[0], x[1]))
        
        for col in groups.keys():
            result.append([val for row, val in groups[col]])
        
        return result