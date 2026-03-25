class Solution:
    def maxCapacity(self, costs: List[int], capacity: List[int], budget: int) -> int:
        arr = [(cost, volume) for cost, volume in zip(costs, capacity) if cost < budget]
        arr.sort(key=lambda p: p[0])
        res = 0
        
        pre_max = [0] * (len(arr) + 1)
        l = 0

        for r in range(len(arr) - 1, -1, -1):

            while l < r and arr[l][0] + arr[r][0] < budget:
                pre_max[l+1] = max(pre_max[l], arr[l][1])
                l += 1
            
            res = max(res, pre_max[min(l, r)] + arr[r][1])
        
        return res
