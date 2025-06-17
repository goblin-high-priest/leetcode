class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        left = min(time)
        right = min(time) * totalTrips

        while left < right:
            mid = (left + right) // 2
            trips = sum([mid // t for t in time])

            if trips < totalTrips:
                left = mid + 1
            else:
                right = mid 
            
        return left

