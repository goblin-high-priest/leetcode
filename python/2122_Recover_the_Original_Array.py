class Solution:
    def recoverArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)

        for i in range(1, n // 2 + 1):
            d = nums[i] - nums[0]

            if d == 0 or d % 2 == 1: continue

            visited = [False] * n
            visited[i] = True
            res = [(nums[0] + nums[i]) >> 1]

            lo, hi = 1, i + 1
            while hi < n:

                while lo < n and visited[lo]:
                    lo += 1
                
                while hi < n and nums[hi] - nums[lo] < d:
                    hi += 1
                
                if hi == n or nums[hi] - nums[lo] > d:
                    break
                
                visited[hi] = True
                res.append((nums[lo] + nums[hi]) >> 1)
                lo += 1
                hi += 1
            
            if len(res) == n // 2: return res
        
        return []