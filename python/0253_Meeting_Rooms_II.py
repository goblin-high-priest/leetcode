class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        if not intervals:
            return 0

        res = 0
        intervals.sort(key=lambda x: x[0])
        heap = []
        
        for start, end in intervals:

            if heap and heap[0] <= start:
                heappop(heap)
            
            heappush(heap, end)
            res = max(res, len(heap))
        
        return res