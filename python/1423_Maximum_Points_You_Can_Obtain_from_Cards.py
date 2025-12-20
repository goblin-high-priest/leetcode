class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        m = len(cardPoints) - k
        res = sum(cardPoints[:m])
        left = 0

        cur = res
        for right in range(m, len(cardPoints)):
            cur += cardPoints[right]
            cur -= cardPoints[left]
            left = right - m + 1
            res = min(res, cur)
        
        return sum(cardPoints) - res
