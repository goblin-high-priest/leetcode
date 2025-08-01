class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        from_ = []
        to = []

        for i, row in enumerate(grid):

            for j, cnt in enumerate(row):

                if cnt > 1:
                    from_.extend([(i, j)] * (cnt - 1))
                elif cnt == 0:
                    to.append((i, j))

        result = float('inf')

        for _from in permutations(from_):
            total = 0

            for (x1, y1), (x2, y2) in zip(_from, to):
                total += abs(x1 - x2) + abs(y1 - y2)
            
            result = min(result, total)
        
        return result