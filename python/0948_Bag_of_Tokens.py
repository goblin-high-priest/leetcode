class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        l, r = 0, len(tokens) - 1
        c = 0
        res = 0

        while l <= r:

            if power >= tokens[l]:
                power -= tokens[l]
                c += 1
                l += 1
            elif power < tokens[l] and c:
                res = max(res, c)
                power += tokens[r]
                c -= 1
                r -= 1
            else:
                break
        
        return max(res, c)