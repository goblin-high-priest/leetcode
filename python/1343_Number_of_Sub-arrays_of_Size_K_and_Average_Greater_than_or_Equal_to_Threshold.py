class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0
        left = 0

        cur = 0
        for right, x in enumerate(arr):
            cur += arr[right]
            left = right - k + 1

            if left < 0: continue
            
            if cur / k >= threshold: res += 1

            cur -= arr[left]
        
        return res
