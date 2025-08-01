class Solution:
    def totalNQueens(self, n: int) -> int:
        col = [False] * n
        diag1 = [False] * (2 * n - 1)
        diag2 = [False] * (2 * n - 1)
        result = 0

        def dfs(r):
            nonlocal result

            if r == n:
                result += 1
                return
            
            for c in range(n):
                is_placed = col[c]

                if not is_placed and not diag1[r+c] and not diag2[r-c]:
                    col[c] = diag1[r+c] = diag2[r-c] = True
                    dfs(r + 1)
                    col[c] = diag1[r+c] = diag2[r-c] = False
                
        dfs(0)

        return result
