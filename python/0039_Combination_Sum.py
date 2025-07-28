class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        path = []
        result = []

        def dfs(i, target):

            if i == len(candidates):
                return

            if target == 0:
                result.append(path[:])
                return
            
            if target < 0:
                return
            
            path.append(candidates[i])
            dfs(i, target - candidates[i])
            path.pop()

            dfs(i + 1, target)

        dfs(0, target)

        return result
