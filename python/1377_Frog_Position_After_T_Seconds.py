class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        g = [[] for _ in range(n + 1)]
        g[1] = [0]

        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
        
        res = 0

        def dfs(x: int, par: int, left_t: int, denominator: int) -> bool:

            if x == target and (left_t == 0 or len(g[x]) == 1):
                nonlocal res
                res = 1 / denominator
                return True
            
            if x == target or left_t == 0: return False

            for y in g[x]:

                if y != par and dfs(y, x, left_t - 1, denominator * (len(g[x]) - 1)):
                    return True
            
            return False
        
        dfs(1, 0, t, 1)

        return res
        