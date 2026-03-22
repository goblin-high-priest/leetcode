class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        return self.tmp(nums1, nums2) + self.tmp(nums2, nums1)
    
    def tmp(self, nums1: List[int], nums2: List[int]) -> int:
        
        res = 0
        
        for target in nums1:
            l, r = 0, len(nums2) - 1

            while l < r:

                if nums2[l] * nums2[r] < target ** 2:
                    l += 1
                elif nums2[l] * nums2[r] > target ** 2:
                    r -= 1
                else:

                    if nums2[l] != nums2[r]:
                        l_tmp, r_tmp = nums2[l], nums2[r]
                        l_mov, r_mov = 0, 0

                        while l < r and nums2[l] == l_tmp:
                            l += 1
                            l_mov += 1
                        
                        while l <= r and nums2[r] == r_tmp:
                            r -= 1
                            r_mov += 1
                        
                        res += l_mov * r_mov
                    else:
                        n = r - l + 1
                        res += n * (n - 1) // 2
                        break
                        
        return res
        