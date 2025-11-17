class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = []

        while columnNumber:
            columnNumber -= 1
            char = chr(ord('A') + columnNumber % 26)
            res.append(char)
            columnNumber = columnNumber // 26
        
        return ''.join(res[::-1])