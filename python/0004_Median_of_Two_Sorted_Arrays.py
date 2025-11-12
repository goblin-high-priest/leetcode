class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a, b = (nums1, nums2) if len(nums1) < len(nums2) else (nums2, nums1)
        length = len(a) + len(b)
        half = length // 2
        left, right = 0, len(a) - 1

        while True:
            i = (left + right) // 2
            j = half - i - 2

            aLeft = a[i] if i >= 0 else float('-inf')
            aRight = a[i+1] if i + 1 < len(a) else float('inf')
            bLeft = b[j] if j >= 0 else float('-inf')
            bRight = b[j+1] if j + 1 < len(b) else float('inf')

            if aLeft <= bRight and bLeft <= aRight:
                
                if length % 2:
                    return min(aRight, bRight)
                else:
                    return (max(aLeft, bLeft) + min(aRight, bRight)) / 2
            elif aLeft > bRight:
                right = i - 1
            else:
                left = i + 1
            

