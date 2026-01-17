class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        cnt = {}
        res = 0

        left = 0
        for right, c in enumerate(s):
            cnt[c] = cnt.get(c, 0) + 1

            while cnt[c] > 2:
                cnt[s[left]] -= 1
                left += 1
        
            res = max(res, right - left + 1)
        
        return res