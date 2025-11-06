class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
        """
        Recursion
        
        Time Complexity: O(n ** 3)
        Space Complexity: O(k * n ** 2)
        """

        n = len(stones)

        if (n - 1) % (k - 1):
            return -1
        
        prefix = list(accumulate(stones, initial=0))

        @cache
        def dfs(i, j, p):

            if p == 1:
                return 0 if i == j else dfs(i, j, k) + prefix[j+1] - prefix[i]
            
            return min(dfs(i, m, 1) + dfs(m + 1, j, p - 1) for m in range(i, j, k - 1))
        
        return dfs(0, n - 1, 1)
