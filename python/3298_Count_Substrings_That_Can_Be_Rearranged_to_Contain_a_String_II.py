class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        cnt1, cnt2 = defaultdict(int), defaultdict(int)
        res = 0

        for c in word2:
            cnt2[c] += 1
        
        diff = len(cnt2)
        
        left = 0
        for c in word1:
            cnt1[c] += 1

            if cnt1[c] == cnt2[c]:
                diff -= 1
            
            while diff == 0:
                left_c = word1[left]
                if cnt1[left_c] == cnt2[left_c]:
                    diff += 1
                
                left += 1
                cnt1[left_c] -= 1
            
            res += left
            
        return res
                