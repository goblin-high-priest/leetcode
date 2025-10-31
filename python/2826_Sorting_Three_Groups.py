class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        g = []
        
        for x in nums:
            i = bisect_right(g, x)

            if i == len(g):
                g.append(x)
            else:
                g[i] = x
            
        return len(nums) - len(g)