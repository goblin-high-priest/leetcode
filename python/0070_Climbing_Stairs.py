class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [-1] * (n + 1)

        def dfs(i):

            if i == 0 or i == 1:
                return 1
            
            if cache[i] != -1:
                return cache[i]

            res = dfs(i - 1) + dfs(i - 2)
            cache[i] = res

            return res

        return dfs(n)