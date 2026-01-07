class Solution:
    def minArrivalsToDiscard(self, arrivals: List[int], w: int, m: int) -> int:
        cnt = defaultdict(int)
        res = 0
        
        for right, x in enumerate(arrivals):

            if cnt.get(x, 0) == m:
                arrivals[right] = -1
                res += 1
            else:
                cnt[arrivals[right]] += 1

            left = right - w + 1

            if left >= 0: cnt[arrivals[left]] -= 1

        return res
