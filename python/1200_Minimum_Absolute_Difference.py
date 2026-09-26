class Solution:
    def minimumAbsDifference(self, arr: list[int]) -> list[list[int]]:
        arr.sort()
        res = []
        diff = float('inf')

        for i in range(1, len(arr)):
            x, y = arr[i-1], arr[i]

            if abs(x - y) < diff:
                diff = abs(x - y)
                res = [[x, y]]
            elif abs(x - y) == diff:
                res.append([x, y])
        
        return res