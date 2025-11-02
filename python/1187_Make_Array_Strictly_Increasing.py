class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        """
        Recursion

        Time Complexity: 
        Space Complexity: 
        """

        # arr2.sort()

        # @cache
        # def dfs(i, pre):

        #     if i < 0:
        #         return 0
            
        #     res = dfs(i - 1, arr1[i]) if arr1[i] < pre else inf
        #     k = bisect_left(arr2, pre) - 1
            
        #     if k >= 0:
        #         res = min(res, dfs(i - 1, arr2[k]) + 1)
            
        #     return res
        
        # res = dfs(len(arr1) - 1, inf)

        # return res if res != inf else -1

        """
        Iteration

        Time Complexity: O(n * (logm + min(n,m))) 
        Space Complexity: O(n)
        """

        a = arr1 + [inf]
        b = sorted(set(arr2))

        @cache
        def dfs(i):
            k = bisect_left(b, a[i])
            res = 0 if k >= i else -inf
            
            if i and a[i-1] < a[i]:
                res = max(res, dfs(i - 1))
            
            for j in range(i - 2, max(i - k - 2, -1), -1):

                if b[k-(i-j-1)] > a[j]:
                    res = max(res, dfs(j))

            return res + 1
        
        res = dfs(len(a) - 1)

        return -1 if res < 0 else len(a) - res
