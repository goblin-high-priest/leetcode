class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key = lambda x: x[0])
        res = [intervals[0]]

        for start, end in intervals:

            if start <= res[-1][1]:
                res[-1] = [res[-1][0], max(res[-1][1], end)]
            else:
                res.append([start, end])
            
        return res