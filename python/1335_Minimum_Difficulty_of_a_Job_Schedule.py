class Solution:
    def minDifficulty(self, jobDifficulty: list[int], d: int) -> int:
        n = len(jobDifficulty)

        if d > n:
            return -1
        
        @cache
        def dfs(start, days_left):

            if days_left == 1:
                return max(jobDifficulty[start:])
            
            best = float("inf")
            day_max = 0

            last_end = n - days_left

            for end in range(start, last_end + 1):
                day_max = max(day_max, jobDifficulty[end])
                remaining_cost = dfs(end + 1, days_left - 1)
                best = min(best, day_max + remaining_cost)
            
            return best
        
        return dfs(0, d)
