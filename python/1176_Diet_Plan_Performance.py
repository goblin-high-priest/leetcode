class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        res = 0

        cur = 0
        for right, x in enumerate(calories):
            cur += x
            left = right - k + 1

            if left < 0: continue

            if cur > upper: res += 1
            if cur < lower: res -= 1

            cur -= calories[left]
        
        return res