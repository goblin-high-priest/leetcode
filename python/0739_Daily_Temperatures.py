class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        From right to left

        Time Complexity: O(n)
        Space Complexity: O(min(n,U)), where U = max(temperatures) − min(temperatures) + 1
        """
        # n = len(temperatures)
        # res = [0] * n
        # stack = []

        # for i in range(n - 1, -1, -1):
        #     t = temperatures[i]

        #     while stack and t >= temperatures[stack[-1]]:
        #         stack.pop()
            
        #     if stack:
        #         res[i] = stack[-1] - i
            
        #     stack.append(i)
        
        # return res

        """
        From left to right

        Time Complexity: O(n)
        Space Complexity: O(min(n,U)), where U = max(temperatures) − min(temperatures) + 1
        """
        n = len(temperatures)
        stack = []
        res = [0] * n

        for i in range(n):

            while stack and temperatures[i] > temperatures[stack[-1]]:
                res[stack[-1]] = i - stack[-1]
                stack.pop()
            
            stack.append(i)
        
        return res