class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        left, right = 0, 0
        res = 0

        cur = 0
        for right in range(len(s)):
            
            if s[right] in "aeiou": cur += 1 

            left = right - k + 1

            if left < 0:
                continue
            
            res = max(res, cur)

            if s[left] in "aeiou": cur -= 1 

        return res
