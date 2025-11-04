class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        """
        Time Complexity: O(nlogn)
        Space Complexity: O(n)
        """

        # g = []
        
        # for x in nums:
        #     i = bisect_right(g, x)

        #     if i == len(g):
        #         g.append(x)
        #     else:
        #         g[i] = x
            
        # return len(nums) - len(g)

        """
        Value-Based

        Time Complexity: O(nU) U = 3
        Space Complexity: O(nU)
        """

        # n = len(nums)
        # f = [[0] * 4 for _ in range(n + 1)]

        # for i, x in enumerate(nums):

        #     for j in range(1, 4):

        #         if j < x:
        #             f[i+1][j] = f[i][j]
        #         else:
        #             f[i+1][j] = max(f[i][j], f[i][x] + 1)
            
        # return n - f[n][3]

        """
        Value-Based with Space Optimized

        Time Complexity: O(nU) U = 3
        Space Complexity: O(U)
        """

        # f = [0] * 4

        # for x in nums:
        #     f[x] += 1
        #     f[2] = max(f[2], f[1])
        #     f[3] = max(f[3], f[2])
        
        # return len(nums) - f[3]

        """
        Value-Based LIS Transition

        Time Complexity: O(nU) U = 3
        Space Complexity: O(U)
        """

        f = [0] * 4

        for x in nums:
            f[x] = max(f[1: x+1]) + 1
        
        return len(nums) - max(f)