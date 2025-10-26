class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_counter, p_counter = {}, {}
        left = 0

        if len(p) > len(s):
            return []

        for i in range(len(p)):
            p_counter[p[i]] = p_counter.get(p[i], 0) + 1
            s_counter[s[i]] = s_counter.get(s[i], 0) + 1
        
        res = [0] if s_counter == p_counter else []

        for right in range(len(p), len(s)):
            s_counter[s[right]] = s_counter.get(s[right], 0) + 1

            if s_counter[s[left]] == 1:
                s_counter.pop(s[left])
            else:
                s_counter[s[left]] -= 1
            
            left += 1

            if s_counter == p_counter:
                res.append(left)
        
        return res
