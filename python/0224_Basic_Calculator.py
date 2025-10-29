class Solution:
    def calculate(self, s: str) -> int:
        cur = res = 0
        sign = 1
        stack = []

        for char in s:

            if char.isdigit():
                cur = cur * 10 + int(char)
            elif char in ['+', '-']:
                res += sign * cur
                sign = 1 if char == '+' else -1
                cur = 0
            elif char == '(':
                stack.append((res, sign))
                sign = 1
                res = 0
            elif char == ')':
                res += sign * cur
                prev_res, prev_sign = stack.pop()
                res = prev_res + prev_sign * res
                cur = 0
        
        return res + sign * cur