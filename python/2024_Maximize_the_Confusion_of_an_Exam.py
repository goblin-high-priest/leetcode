class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        res = 0
        cnt = defaultdict(int)

        left = 0
        for right, c in enumerate(answerKey):
            cnt[c] += 1

            while cnt['T'] > k and cnt['F'] > k:
                a = answerKey[left]
                cnt[a] -= 1
                left += 1
            
            res = max(res, right - left + 1)
        
        return res
