class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        res = 0
        cnt = [0, 0]

        left = 0
        for right, x in enumerate(s):
            cnt[ord(x)&1] += 1

            while cnt[0] > k and cnt[1] > k:
                cnt[ord(s[left])&1] -= 1
                left += 1
            
            res += right - left + 1
        
        return res