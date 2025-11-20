class Solution:
    def maxOutput(self, n: int, edges: List[List[int]], price: List[int]) -> int:
        g = [[] for _ in range(n)]

        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
        
        res = 0

        def dfs(x: int, par: int) -> (int, int):
            nonlocal res
            max_s1 = p = price[x]
            max_s2 = 0

            for y in g[x]:

                if y != par:
                    s1, s2 = dfs(y, x)
                    res = max(res, s1 + max_s2, s2 + max_s1)
                    max_s1 = max(max_s1, s1 + p)
                    max_s2 = max(max_s2, s2 + p)
                
            return max_s1, max_s2
        
        dfs(0, -1)

        return res