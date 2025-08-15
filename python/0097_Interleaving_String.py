class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n, m = len(s1), len(s2)

        if n + m != len(s3):
            return False
        
        @cache
        def dfs(i, j):

            if i < 0 and j < 0:
                return True
            
            return i >= 0 and s3[i+j+1] == s1[i] and dfs(i - 1, j) or \
                   j >= 0 and s3[i+j+1] == s2[j] and dfs(i, j - 1)
        
        return dfs(n - 1, m - 1)