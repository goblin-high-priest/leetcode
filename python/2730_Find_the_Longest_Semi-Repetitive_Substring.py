class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        same = 0
        left = 0
        res = 0

        for right in range(len(s)):

            if right > 0 and s[right] == s[right-1]:
                if same == 0:
                    same = 1
                    res = max(res, right - left + 1)
                else:
                    while s[left] != s[left+1] and left <= right:
                        left += 1
                    left += 1
            
            res = max(res, right - left + 1)
        
        return res