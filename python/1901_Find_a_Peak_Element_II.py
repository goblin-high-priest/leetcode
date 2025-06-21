class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        left, right = 0, len(mat) - 1

        while left < right:
            row_idx = (left + right) // 2
            cur_val = max(mat[row_idx])
            col_idx = mat[row_idx].index(cur_val)

            if cur_val < mat[row_idx+1][col_idx]:
                left = row_idx + 1
            else:
                right = row_idx
            
        return [left, mat[left].index(max(mat[left]))]