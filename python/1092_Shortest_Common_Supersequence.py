class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        
        @cache
        def dfs(i, j):
            
            if i < 0:
                return j + 1
            
            if j < 0:
                return i + 1
            
            if str1[i] == str2[j]:
                return dfs(i - 1, j - 1) + 1
            
            return min(dfs(i - 1, j), dfs(i, j - 1)) + 1
        
        def make_ans(i, j):
            
            if i < 0:
                return str2[:j+1]
            
            if j < 0:
                return str1[:i+1]

            if str1[i] == str2[j]:
                return make_ans(i - 1, j - 1) + str1[i]
            
            if dfs(i, j) == dfs(i - 1, j) + 1:
                return make_ans(i - 1, j) + str1[i]
            
            return make_ans(i, j - 1) + str2[j]
        
        return make_ans(len(str1) - 1, len(str2) - 1)
