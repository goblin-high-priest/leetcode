class Solution:
    def minWindow(self, s: str, t: str) -> str:
        cnt_s = Counter()
        cnt_t = Counter(t)
        is_found = False
        left = 0
        res = float('inf')

        for right, c in enumerate(s):
            cnt_s[c] += 1

            while cnt_s >= cnt_t:
                is_found = True
                if right - left + 1 < res:
                    res = right - left + 1 
                    left_, right_ = left, right

                cnt_s[s[left]] -= 1
                left += 1
            
        return s[left_:right_+1] if is_found else ""