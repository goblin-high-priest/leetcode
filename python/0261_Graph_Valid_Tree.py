class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        mapping = defaultdict(list)
        
        for s, t in edges:
            mapping[s].append(t)
            mapping[t].append(s)
        
        visited = set()

        def dfs(prev, i):
            
            if i not in visited:
                visited.add(i)
            else:
                return False
            
            for j in mapping[i]:

                if j == prev:
                    continue
                
                if not dfs(i, j):
                    return False
            
            return True
        
        return dfs(-1, 0) and n == len(visited)
