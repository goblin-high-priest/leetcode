class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        """
        Recursion

        Time Complexity: O(n ** 2)
        Space Complexity: O(n ** 2)
        """

        # n = len(s)

        # @cache
        # def dfs(i, j):

        #     if i > j:
        #         return 0
            
        #     if i == j:
        #         return 1
            
        #     if s[i] == s[j]:
        #         return 2 + dfs(i + 1, j - 1)
            
        #     return max(dfs(i + 1, j), dfs(i, j - 1))
        
        # return dfs(0, n - 1)

        """
        Iteration

        Time Complexity: O(n ** 2)
        Space Complexity: O(n ** 2)
        """

        # n = len(s)
        # f = [[0] * n for _ in range(n)]

        # for i in range(n - 1, -1, -1):
        #     f[i][i] = 1

        #     for j in range(i + 1, n):
                
        #         if s[i] == s[j]:
        #             f[i][j] = f[i+1][j-1] + 2
        #         else:
        #             f[i][j] = max(f[i+1][j], f[i][j-1])
            
        # return f[0][-1]

        """
        Iteration with Space Optimized

        Time Complexity: O(n ** 2)
        Space Complexity: O(n)
        """

        n = len(s)
        f = [0] * n

        for i in range(n - 1, -1, -1):
            f[i] = 1
            pre = 0   # f[i+1][i]

            for j in range(i + 1, n):
                tmp = f[j]
                f[j] = pre + 2 if s[i] == s[j] else max(f[j], f[j-1])
                pre = tmp
            
        return f[-1]
