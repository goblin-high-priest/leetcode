class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        g = [[] for _ in range(n)]

        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
        
        cnt = [0] * n

        def dfs(x: int, par: int, target: int) -> bool:

            if x == target:
                cnt[x] += 1
                return True
            
            for y in g[x]:
                
                if y != par and dfs(y, x, target):
                    cnt[x] += 1
                    return True
            
            return False
        
        for start, end in trips:
            dfs(start, -1, end)
        
        def dfs(x: int, par: int) -> Tuple[int, int]:
            not_halve = price[x] * cnt[x]
            halve = not_halve // 2

            for y in g[x]:

                if y != par:
                    nh, h = dfs(y, x)
                    not_halve += min(nh, h)
                    halve += nh
                
            return not_halve, halve
        
        return min(dfs(0, -1))
