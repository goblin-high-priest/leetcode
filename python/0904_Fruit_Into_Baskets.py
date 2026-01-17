class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        cnt = defaultdict(int)
        res = 0

        left = 0
        for right, x in enumerate(fruits):
            cnt[x] += 1

            while len(cnt) > 2:
                cnt[fruits[left]] -= 1

                if cnt[fruits[left]] == 0: del cnt[fruits[left]]

                left += 1
            
            res = max(res, right - left + 1)
        
        return res