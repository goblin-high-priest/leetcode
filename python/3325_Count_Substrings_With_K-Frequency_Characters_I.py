class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        res = 0
        cnt = defaultdict(int)

        left = 0    
        for c in s:
            cnt[c] += 1

            while cnt[c] == k:
                left_c = s[left]
                cnt[left_c] -= 1
                left += 1
            
            res += left
        
        return res