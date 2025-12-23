class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        cnt = Counter(s)
        res = 0

        if k == 0:
            return 0
        
        if any(c not in s for c in "abc"):
            return -1

        for c in cnt:
            
            if cnt[c] < k:
                return -1
        
        left = 0
        for right, c in enumerate(s):
            cnt[c] -= 1
            
            while cnt[c] < k:
                cnt[s[left]] += 1
                left += 1
            
            res = max(res, right - left + 1)
        
        return len(s) - res
            