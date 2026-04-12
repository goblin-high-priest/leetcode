class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        def generate(lock):
            res = []

            for i in range(4):
                res.append(lock[:i] + str((int(lock[i]) + 1) % 10) + lock[i+1:])
                res.append(lock[:i] + str((int(lock[i]) - 1 + 10) % 10) + lock[i+1:])
            
            return res
        
        if "0000" in deadends:
            return -1
        
        if "0000" == target:
            return 0
        
        q = deque()
        visited = set(deadends)
        q.append(["0000", 0])
        while q:
            lock, turn = q.popleft()
            turn += 1

            if lock in visited:
                continue

            visited.add(lock)
            
            for l in generate(lock):
                
                if l == target:
                    return turn
                
                q.append([l, turn])
        
        return -1
