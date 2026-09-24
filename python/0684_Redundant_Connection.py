class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        par = [i for i in range(len(edges) + 1)]
        rank = [1 for _ in range(len(edges) + 1)]

        def find(node):

            if node == par[node]:
                return node
            
            return find(par[node])
        
        def union(node1, node2):
            root1, root2 = find(node1), find(node2)

            if root1 == root2:
                return False
            
            if rank[root1] < rank[root2]:
                rank[root2] += rank[root1]
                par[root1] = root2
            else:
                rank[root1] += rank[root2]
                par[root2] = root1
            
            return True
        
        for node1, node2 in edges:

            if not union(node1, node2):
                return [node1, node2]
