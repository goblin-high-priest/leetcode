class Solution:
    def maximumCoins(self, coins: List[List[int]], k: int) -> int:
        segments = sorted(coins)

        starts = [left for left, right, count in segments]

        prefix = [0]

        res = 0

        for left, right, count in segments:
            total = (right - left + 1) * count
            prefix.append(prefix[-1] + total)
        
        def count_up_to(x):
            i = bisect_right(starts, x) - 1

            if i < 0:
                return 0
            
            left, right, count = segments[i]

            length = min(x, right) - left + 1

            return prefix[i] + length * count
        
        for left, right, _ in segments:
            start_at_left = (count_up_to(left + k - 1) - count_up_to(left - 1))
            end_at_right = (count_up_to(right) - count_up_to(right - k))

            res = max(res, start_at_left, end_at_right)

        return res
