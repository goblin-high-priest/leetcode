class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0
        intervals = sorted(intervals, key=lambda x: (x[0], x[1]))
        # intervals.sort()
        prevEnd = intervals[0][1]

        for interval in intervals[1:]:

            if interval[0] >= prevEnd:
                prevEnd = interval[1]
            else:
                res += 1
                prevEnd = min(prevEnd, interval[1])
        
        return res
    