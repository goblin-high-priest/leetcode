class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        n = len(s)
        p = pow(power, k - 1, modulo)
        h = res = 0

        for i in range(n - 1, -1, -1):
            h = (h * power + ord(s[i]) % 96) % modulo
            right = i + k - 1

            if right >= n: continue

            if h == hashValue: res = i

            h = (h - ord(s[right]) % 96 * p + modulo) % modulo

        return s[res: res + k]
