class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        
        def diameter(edges):
            g = [[] for _ in range(len(edges) + 1)]

            for x, y in edges:
                g[x].append(y)
                g[y].append(x)
            
            res = 0

            def dfs(x, par):
                nonlocal res
                max_len = 0

                for y in g[x]:
                    
                    if y != par:
                        cur_len = 1 + dfs(y, x)
                        res = max(res, max_len + cur_len)
                        max_len = max(max_len, cur_len)
                    
                return max_len
            
            dfs(0, -1)

            return res
        
        d1, d2 = diameter(edges1), diameter(edges2)
        
        return max(d1, d2, (d1 + 1) // 2 + (d2 + 1) // 2 + 1)
