@cache
def dfs(i, n):
    
    if n < i ** 2:
        return dfs(i - 1, n)

    if i == 0:
        return 0 if n == 0 else inf
    
    return min(1 + dfs(i, n - i ** 2), dfs(i - 1, n))

class Solution:
    def numSquares(self, n: int) -> int:
        i = int(sqrt(n))
    
        return dfs(i, n)