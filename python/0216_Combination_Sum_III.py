class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        path = []
        result = []

        def dfs(i, left_sum):
            remaining_count = k - len(path)
            # prune
            if left_sum < 0 or left_sum > (i + i - remaining_count + 1) * remaining_count // 2:
                return

            if len(path) == k:

                if left_sum == 0:
                    result.append(path[:])
                    return

                return
            
            for j in range(i, 0, -1):
                path.append(j)
                dfs(j - 1, left_sum - j)
                path.pop()

        dfs(9, n)

        return result