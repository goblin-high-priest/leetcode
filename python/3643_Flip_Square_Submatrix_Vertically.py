class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        top, bottom = x, x + k - 1

        while top < bottom:

            for i in range(k):
                grid[top][y+i], grid[bottom][y+i] = grid[bottom][y+i], grid[top][y+i]
            
            top += 1
            bottom -= 1
        
        return grid