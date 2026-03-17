class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        res = deque()
        i = bisect_left(arr, x) - 1
        l, r = i, i + 1

        while k > 0:

            if l < 0:
                res.append(arr[r])
                r += 1
                k -= 1
                continue
            
            if r >= len(arr):
                res.appendleft(arr[l])
                l -= 1
                k -= 1
                continue
            
            if math.fabs(x - arr[l]) <= math.fabs(x - arr[r]):
                res.appendleft(arr[l])
                l -= 1
                k -= 1
            else:
                res.append(arr[r])
                r += 1
                k -= 1
        
        return list(res)