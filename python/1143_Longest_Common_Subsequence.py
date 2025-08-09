# class Solution:
#     def longestCommonSubsequence(self, text1: str, text2: str) -> int:
#         i = len(text1)
#         j = len(text2)

#         @cache
#         def dfs(i, j):

#             if i < 0 or j < 0:
#                 return 0
            
#             if text1[i] == text2[j]:
#                 return 1 + dfs(i - 1, j - 1)
            
#             return max(dfs(i - 1, j), dfs(i, j - 1))
        
#         return dfs(i - 1, j - 1)

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        i = len(text1)
        j = len(text2)
        f = [0] * (j + 1)

        for x in text1:
            pre = 0

            for j, y in enumerate(text2):
                tmp = f[j+1]
                f[j+1] = pre + 1 if x == y else max(f[j+1], f[j])
                pre = tmp
            
        return f[-1]