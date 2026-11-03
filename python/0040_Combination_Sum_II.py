class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        res, path = [], []

        def dfs(start, remain):

            if remain == 0:
                res.append(path[:])
                return

            for i in range(start, len(candidates)):

                if candidates[i] > remain:
                    break

                if i > start and candidates[i] == candidates[i-1]:
                    continue

                path.append(candidates[i])

                dfs(i + 1, remain - candidates[i])

                path.pop()

        dfs(0, target)

        return res
