class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        scores = [0] * (n + 1)

        for a, b in trust:
            scores[a] -= 1
            scores[b] += 1
        
        for person in range(1, n + 1):
            
            if scores[person] == n - 1:
                return person
        
        return -1