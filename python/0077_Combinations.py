class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        path = []
        result = []

        def dfs(n):
            count = k - len(path)

            if count == 0:
                result.append(path[:])
                return
            # Setting the lower bound as count - 1 instead of 0 for pruning.
            for i in range(n, count - 1, -1):
                path.append(i)
                dfs(i - 1)
                path.pop()
            
        dfs(n)

        return result
