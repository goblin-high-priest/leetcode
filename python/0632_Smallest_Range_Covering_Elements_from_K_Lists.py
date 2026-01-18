class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        pairs = sorted((x, i) for (i, arr) in enumerate(nums) for x in arr)
        res_l, res_r = -inf, inf
        category = len(nums)
        cnt = [0] * category
        left = 0
        l = -inf

        for r, i in pairs:

            if cnt[i] == 0:
                category -= 1
            
            cnt[i] += 1
            while category == 0:
                l, i = pairs[left]
                cnt[i] -= 1

                if cnt[i] == 0: category += 1

                left += 1
            
            if r - l < res_r - res_l:
                res_l, res_r = l, r
            
        return [res_l, res_r]
