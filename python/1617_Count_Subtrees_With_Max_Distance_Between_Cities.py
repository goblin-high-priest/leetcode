class Solution:
    def countSubgraphsForEachDiameter(self, n: int, edges: List[List[int]]) -> List[int]:
        g = [[] for _ in range(n)]

        for x, y in edges:
            g[x-1].append(y - 1)
            g[y-1].append(x - 1)
        
        res = [0] * (n - 1)
        in_set = [False] * n

        def f(i: int) -> None:

            if i == n:
                visited = [False] * n
                diameter = 0

                for v, b in enumerate(in_set):

                    if not b: continue

                    def dfs(x: int) -> int:
                        nonlocal diameter
                        visited[x] = True
                        max_len = 0

                        for y in g[x]:

                            if not visited[y] and in_set[y]:
                                cur_len = dfs(y) + 1
                                diameter = max(diameter, max_len + cur_len)
                                max_len = max(max_len, cur_len)
                            
                        return max_len
                    
                    dfs(v)

                    break
                
                if diameter and visited == in_set:
                    res[diameter-1] += 1
                
                return
            
            f(i + 1)

            in_set[i] = True
            f(i + 1)
            in_set[i] = False

        f(0)
        
        return res
