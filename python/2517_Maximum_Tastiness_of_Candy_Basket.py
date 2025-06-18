"""
    This algorithm is adapted from
    https://leetcode.cn/problems/maximum-tastiness-of-candy-basket/solutions/2031994/er-fen-da-an-by-endlesscheng-r418/
"""
class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        def f(d):
            cnt = 1
            pre = price[0]

            for p in price:

                if p >= pre + d:
                    cnt += 1
                    pre = p
            
            return cnt
        
        price.sort()
        left, right = 0, (price[-1] - price[0]) // (k - 1) + 1

        while left < right:
            mid = (left + right) // 2

            if f(mid) >= k:
                left = mid + 1
            else:
                right = mid

        return left - 1
