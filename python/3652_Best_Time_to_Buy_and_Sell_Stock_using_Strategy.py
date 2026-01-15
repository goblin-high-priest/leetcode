class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)
        s = list(accumulate((p * s for p, s in zip(prices, strategy)), initial=0))
        s_sell = list(accumulate(prices, initial=0))

        res = max(s[i-k] + s[n] - s[i] + s_sell[i] - s_sell[i-k//2] for i in range(k, n + 1))
        return max(res, s[n])