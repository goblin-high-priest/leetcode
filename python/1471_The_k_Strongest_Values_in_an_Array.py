class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        l, r = 0, len(arr) - 1
        res = []
        arr.sort()
        center_idx = (len(arr) - 1) // 2
        center = arr[center_idx]

        while k > 0 and l <= r:
            lv, rv = arr[l], arr[r]

            if math.fabs(lv - center) <= math.fabs(rv - center):
                res.append(rv)
                r -= 1
                k -= 1
            else:
                res.append(lv)
                l += 1
                k -= 1
        
        return res
