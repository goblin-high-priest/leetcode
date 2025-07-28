class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        path = []
        result = []

        def dfs(i):
            right_parenthe = len(path) - i

            if len(path) == 2 * n:
                result.append(''.join(path))
                return
            
            if i < n:
                path.append('(')
                dfs(i + 1)
                path.pop()

            if right_parenthe < i:
                path.append(')')
                dfs(i)
                path.pop()
            
        dfs(0)

        return result