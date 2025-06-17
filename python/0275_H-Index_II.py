class Solution:
    def hIndex(self, citations: List[int]) -> int:
        left = 1
        right = len(citations) + 1
        
        while left < right:
            mid = (left + right) // 2

            if citations[-mid] >= mid:
                left = mid + 1
            else:
                right = mid
            
        return left - 1