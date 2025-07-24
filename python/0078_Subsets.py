class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)
        path = []

        if n == 0:
            return []

        def dfs(i):

            if i == n:
                result.append(path.copy())
                return
            
            dfs(i + 1)
            path.append(nums[i])
            dfs(i + 1)
            path.pop()
        
        dfs(0)

        return result
