class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
        res = []

        while top <= bottom and left <= right:

            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1

            for j in range(top, bottom + 1):
                res.append(matrix[j][right])
            right -= 1

            if top > bottom or left > right:
                break

            for i in range(right, left - 1, -1):
                res.append(matrix[bottom][i])
            bottom -= 1

            for j in range(bottom, top - 1, -1):
                res.append(matrix[j][left])
            left += 1
        
        return res