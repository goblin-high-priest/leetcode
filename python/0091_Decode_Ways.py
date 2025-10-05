class Solution:
    # def numDecodings(self, s: str) -> int:
    #     n = len(s)
        
    #     @cache
    #     def dfs(i):
    #         res = 0

    #         if i < 0:
    #             return 1
            
    #         if 1 <= int(s[i]) <= 9:
    #             res += dfs(i - 1)

    #         if i >= 1 and 10 <= int(s[i-1:i+1]) <= 26:
    #             res += dfs(i - 2)
            
    #         return res

    #     return dfs(n - 1)
    def numDecodings(self, s: str) -> int:
        n = len(s)
        
        if s[0] == "0":
            return 0
        
        prev0, prev1 = 1, 1

        for i in range(1, n):
            cur = 0

            if s[i] != "0":
                cur += prev1
            
            if 10 <= int(s[i-1:i+1]) <= 26:
                cur += prev0
            
            prev0, prev1 = prev1, cur
        
        return prev1