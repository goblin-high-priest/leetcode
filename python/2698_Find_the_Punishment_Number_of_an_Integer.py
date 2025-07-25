PRE_SUM = [0] * 1001

for i in range(1, 1001):
    s = str(i * i)
    n = len(s)

    def dfs(pos, sum):
        
        if pos == n:
            return sum == i
        
        x = 0

        for j in range(pos, n):
            x = x * 10 + int(s[j])

            if dfs(j + 1, sum + x):
                return True
            
        return False
    
    PRE_SUM[i] = PRE_SUM[i-1] + (i * i if dfs(0, 0) else 0)
    
class Solution:
    def punishmentNumber(self, n: int) -> int:
        return PRE_SUM[n]
