class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        queens = [0] * n
        col = [False] * n
        diag1 = [False] * (n * 2 - 1)
        diag2 = [False] * (n * 2 - 1)

        def dfs(r):
            
            if r == n:
                result.append(['.' * c + 'Q' + '.' * (n - 1 - c) for c in queens])
                return
            
            for c, placed in enumerate(col):

                if not placed and not diag1[r + c] and not diag2[r - c]:
                    queens[r] = c
                    col[c] = diag1[r + c] = diag2[r - c] = True
                    dfs(r + 1)
                    col[c] = diag1[r + c] = diag2[r - c] = False
                
        dfs(0)

        return result