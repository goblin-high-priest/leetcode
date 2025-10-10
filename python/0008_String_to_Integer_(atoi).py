class Solution:
    def myAtoi(self, s: str) -> int:
        MAX_INT = 2 ** 31 - 1
        MIN_INT = -2 ** 31
        s = s.lstrip()
        i = 0
        res = 0
        sign = 1

        if not s:
            return 0

        if s[0] == '-':
            sign = -1
            i += 1
        elif s[0] == '+':
            i += 1

        while i < len(s):

            if s[i].isdigit():
                res = res * 10 + int(s[i]) 
                i += 1
            else:
                break
            
        return min(MAX_INT, res) if sign == 1 else max(MIN_INT, sign * res)
