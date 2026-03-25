class Solution:
    def countPairs(self, n: int, edges: List[List[int]], queries: List[int]) -> List[int]:
        deg = [0] * (n + 1)

        for x, y in edges:
            deg[x] += 1
            deg[y] += 1
        
        cnt_e = Counter(tuple(sorted(e)) for e in edges)
        
        res = [0] * len(queries)
        sorted_deg = sorted(deg)

        for j, q in enumerate(queries):
            left, right = 1, n

            while left < right:

                if sorted_deg[left] + sorted_deg[right] <= q:
                    left += 1
                else:
                    res[j] += right - left
                    right -= 1
            
            for (x, y), c in cnt_e.items():

                if q < deg[x] + deg[y] <= q + c:
                    res[j] -= 1
            
        return res