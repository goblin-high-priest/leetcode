COLUMN = 6
get_dis = lambda a, b: abs(a // COLUMN - b // COLUMN) + abs(a % COLUMN - b % COLUMN)
dis = [[get_dis(i, j) for j in range(26)] for i in range(26)]
class Solution:
    def minimumDistance(self, word: str) -> int:
        word = [ord(ch) - ord('A') for ch in word]

        @cache
        def dfs(i: int, finger1: int, finger2: int) -> int:

            if i < 0:
                return 0

            res1 = dfs(i - 1, word[i], finger2) + dis[finger1][word[i]]
            res2 = dfs(i - 1, finger1, word[i]) + dis[finger2][word[i]]

            return min(res1, res2)
        
        n = len(word)

        return min(dfs(n - 2, finger1, word[-1]) for finger1 in range(26))