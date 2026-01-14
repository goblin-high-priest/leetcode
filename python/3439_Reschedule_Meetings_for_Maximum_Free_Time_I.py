class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        free = [0] * (n + 1)
        free[0] = startTime[0]
        free[n] = eventTime - endTime[-1]

        for i in range(1, n):
            free[i] = startTime[i] - endTime[i-1]
        
        cur = res = 0
        for right, x in enumerate(free):
            cur += x

            if right < k: continue

            res = max(res, cur)
            cur -= free[right-k]
        
        return res
