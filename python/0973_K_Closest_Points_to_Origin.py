class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        minHeap method 

        Time Complexity: O(n + klogn)
        """

        # minHeap = []
        # res = []

        # for x, y in points:
        #     dist = x ** 2 + y ** 2
        #     minHeap.append((dist, x, y))
        
        # heapq.heapify(minHeap)

        # for _ in range(k):
        #     dist, x, y = heapq.heappop(minHeap)
        #     res.append([x, y])
        
        # return res

        """
        maxHeap method 

        Time Complexity: O(nlogk)
        """

        maxHeap = []
        res = []

        for x, y in points:
            dist = x ** 2 + y ** 2

            if len(maxHeap) < k:
                heapq.heappush(maxHeap, (-dist, x, y))
            else:
                heapq.heappush(maxHeap, (-dist, x, y))
                heapq.heappop(maxHeap)
            
        return [[x, y] for _, x, y in maxHeap]