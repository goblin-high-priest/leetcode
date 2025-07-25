class Solution:
    def partition(self, s: str) -> List[List[str]]:  
        result = []
        path = []
        n = len(s)

        if n == 0:
            return []

        def dfs(start):

            if start == n:
                result.append(path[:])
                return
            
            for end in range(start + 1, n + 1):
                sub = s[start:end]

                if sub == sub[::-1]:
                    path.append(sub)
                    dfs(end)
                    path.pop()
                    
        dfs(0)

        return result
