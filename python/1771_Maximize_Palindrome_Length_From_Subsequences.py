class Solution:
    def longestPalindrome(self, word1: str, word2: str) -> int:
        """
        Recursion
        
        Time Complexity: O((n + m) ** 2)
        Space Complexity: O((n + m) ** 2)
        """

        # s = word1 + word2
        # n = len(s)
        # res = [0]

        # @cache
        # def dfs(i, j):

        #     if i > j:
        #         return 0
        #     elif i == j:
        #         return 1
            
        #     if s[i] == s[j]:
        #         tmp = dfs(i + 1, j - 1) + 2

        #         if i < len(word1) <= j:
        #             res[0] = max(res[0], tmp)

        #         return tmp

        #     return max(dfs(i + 1, j), dfs(i, j - 1))
        
        # dfs(0, n - 1)

        # return res[0]

        """
        Iteration
        
        Time Complexity: O((n + m) ** 2)
        Space Complexity: O((n + m) ** 2)
        """

        s = word1 + word2
        res, n = 0, len(s)
        f = [[0] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            f[i][i] = 1

            for j in range(i + 1, n):

                if s[i] == s[j]:
                    f[i][j] = f[i+1][j-1] + 2

                    if i < len(word1) <= j:
                        res = max(res, f[i][j])
                else:
                    f[i][j] = max(f[i+1][j], f[i][j-1])
        
        return res
