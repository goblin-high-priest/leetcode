class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        res = 0
        q = deque()
        s = left = 0

        for i, x in enumerate(chargeTimes):
            
            while q and x >= chargeTimes[q[-1]]:
                q.pop()
            q.append(i)
            s += runningCosts[i]

            while q and chargeTimes[q[0]] + (i - left + 1) * s > budget:
                
                if q[0] == left:
                    q.popleft()
                
                s -= runningCosts[left]
                left += 1
                 
            
            if q: res = max(res, i - left + 1)

        return res