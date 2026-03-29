class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        res = 0
        s = str(num)

        for i in range(len(s) - k + 1):
            divisor = int(s[i:i+k])

            if divisor > 0 and num % divisor == 0:
                res += 1
        
        return res