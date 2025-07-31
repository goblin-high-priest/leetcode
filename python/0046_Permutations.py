class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        path = [0] * n
        result = []
        on_path = [False] * n

        def dfs(i):

            if i == n:
                result.append(path[:])
                return
            
            for j, num in enumerate(nums):

                if not on_path[j]:
                    on_path[j] = True
                    path[i] = num
                    dfs(i + 1)
                    on_path[j] = False
                
        dfs(0)

        return result
