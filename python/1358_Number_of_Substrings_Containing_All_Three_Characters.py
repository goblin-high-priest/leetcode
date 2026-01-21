class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        cnt = defaultdict(int)
        res = 0

        left = 0
        for right, c in enumerate(s):
            cnt[c] += 1

            while len(cnt) == 3:
                left_c = s[left]
                cnt[left_c] -= 1

                if cnt[left_c] == 0: del cnt[left_c]

                left += 1
            res += left 
        
        return res