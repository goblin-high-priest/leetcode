class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0  
        stack = [] # tuple: index, height

        for i, h in enumerate(heights):
            start = i

            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            
            stack.append((start, h))

        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        
        return maxArea


    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        n = len(matrix[0])
        res = 0
        heights = [0] * n

        for row in matrix:

            for i, h in enumerate(row):
                
                if h == '0':
                    heights[i] = 0
                else:
                    heights[i] += 1
                
            res = max(res, self.largestRectangleArea(heights))
        
        return res