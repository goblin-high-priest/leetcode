# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        arr = []
        result = []

        def dfs(root):
            
            if root is None:
                return
            
            dfs(root.left)

            arr.append(root.val)

            dfs(root.right)

        dfs(root)

        n = len(arr)

        for q in queries:
            pos = bisect_left(arr, q)
            
            mx = arr[pos] if pos < n else -1

            if pos == n or arr[pos] != q:
                pos -= 1

            mn = arr[pos] if pos >= 0 else -1
            result.append([mn, mx])
        
        return result