class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        max_LIS = 0

        g = []
        prefix = [0] * n

        for i, x in enumerate(nums):
            j = bisect_left(g, x)
            
            if j == len(g):
                g.append(x)
            else:
                g[j] = x

            prefix[i] = j + 1
        
        g = []
        suffix = [0] * n

        for i in range(n - 1, -1, -1):
            x = nums[i]
            j = bisect_left(g, x)
            
            if j == len(g):
                g.append(x)
            else:
                g[j] = x

            suffix[i] = j + 1

        for i in range(n):
            pre, suf = prefix[i], suffix[i]

            if pre >= 2 and suf >= 2:
                max_LIS = max(max_LIS, pre + suf - 1)
            
        return n - max_LIS
