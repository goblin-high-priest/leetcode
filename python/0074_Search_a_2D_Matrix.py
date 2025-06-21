class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        first_column = [row[0] for row in matrix]
        row_index = bisect_right(first_column, target) - 1
        column_index = bisect_right(matrix[row_index], target) - 1

        return True if target == matrix[row_index][column_index] else False
