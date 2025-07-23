class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {1: '', 2: 'abc',3: 'def',4: 'ghi',5: 'jkl',6: 'mno',7: 'pqrs',8: 'tuv',9: 'wxyz'}
        result = []
        n = len(digits)
        path = [''] * n

        if n == 0:
            return []

        def dfs(i):
            
            if i == n:
                result.append("".join(path))
                return

            for char in mapping[int(digits[i])]:
                path[i] = char
                dfs(i + 1)
            
        dfs(0)

        return result
