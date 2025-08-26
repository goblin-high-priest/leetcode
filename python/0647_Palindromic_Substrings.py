class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        def countPali(l, r):
            nonlocal res

            while l >= 0 and r < len(s) and s[l] == s[r]:
                
                res += 1
                l -= 1
                r += 1

        for i in range(len(s)):
            countPali(i, i)
            countPali(i, i + 1)
        
        return res
