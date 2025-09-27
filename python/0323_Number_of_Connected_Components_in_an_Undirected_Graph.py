class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        rank = [1] * n
        res = n

        def find(m):

            while m != parent[m]:
                parent[m] = parent[parent[m]]
                m = parent[m]
            
            return m
        
        def union(m1, m2):
            p1, p2 = find(m1), find(m2)

            if p1 == p2:
                return 0
            
            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            
            return 1
        
        for m1, m2 in edges:
            res -= union(m1, m2)
        
        return res
