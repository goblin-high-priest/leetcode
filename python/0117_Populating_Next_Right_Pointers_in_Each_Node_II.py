"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':

        if root is None:
            return None

        q = [root]

        while q:

            for x, y in pairwise(q):
                x.next = y

            tmp = q
            q = []

            for node in tmp:

                if node.left:
                    q.append(node.left)
                
                if node.right:
                    q.append(node.right)
                
        return root
