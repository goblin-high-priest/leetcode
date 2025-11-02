class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        """
        DP

        Time Complexity: O(n ** 2)
        Space Complexity: O(n)
        """

        # n = len(ages)
        # dp = [0] * n
        # sa = sorted(zip(scores, ages))

        # for i, (score, age) in enumerate(sa):
            
        #     for j in range(i):
        #         cur_age = sa[j][1]

        #         if cur_age <= age:
        #             dp[i] = max(dp[i], dp[j])
                
        #     dp[i] += score
        
        # return max(dp)

        """
        value-based DP

        Time Complexity: O(nU) where U = max(ages)
        Space Complexity: O(n + U)
        """

        max_sum = [0] * (max(ages) + 1)

        for score, age in sorted(zip(scores, ages)):
            max_sum[age] = max(max_sum[:age+1]) + score
        
        return max(max_sum)
