class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()

        def dfs(r, c, i):

            if i == len(word):
                return True
            
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or (r, c) in path or word[i] != board[r][c]:
                return False
            
            path.add((r, c))
            
            for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:

                if dfs(r + dx, c + dy, i + 1):
                    return True
            path.remove((r, c))



        for r in range(ROWS):

            for c in range(COLS):

                if dfs(r, c, 0):
                    return True
        
        return False
