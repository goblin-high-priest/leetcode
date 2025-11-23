class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        stack = []
        res = 0

        for i, h in enumerate(nums):
            start = i

            while stack and h <= stack[-1][1]:
                index, height = stack.pop()

                if index <= k <= i - 1:
                    res = max(res, height * (i - index))
                
                start = index
                
            stack.append((start, h))
        
        for start, h in stack:
            
            if start <= k:
                res = max(res, h * (len(nums) - start))
        
        return res
                    