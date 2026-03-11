class Solution:
    def reverseWords(self, s: str) -> str:
        i = 0
        l = 0
        s = list(s)

        while i <= len(s):

            if i == len(s) or s[i] == ' ':
                r = i - 1

                while l < r:
                    s[l], s[r] = s[r], s[l]
                    l += 1
                    r -= 1
                
                l = i + 1
            
            i += 1
        
        return ''.join(s)