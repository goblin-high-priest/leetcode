class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        res = s

        if s.count('1') < k:
            return ""
        
        cnt1 = left = 0
        for right, c in enumerate(s):
            cnt1 += int(c)

            while cnt1 > k or s[left] == '0':
                cnt1 -= int(s[left])
                left += 1
            
            if cnt1 == k:
                tmp = s[left:right+1]

                if len(tmp) < len(res) or len(tmp) == len(res) and tmp < res:
                    res = tmp
            
        return res