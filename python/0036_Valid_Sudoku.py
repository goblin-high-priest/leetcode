class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        square = defaultdict(set)

        for r in range(9):
            for c in range(9):
                v = board[r][c]

                if v == '.': continue

                if v in rows[r] or v in cols[c] or v in square[(r // 3, c // 3)]:
                    return False
                
                rows[r].add(v)
                cols[c].add(v)
                square[(r // 3, c // 3)].add(v)
        
        return True
