class Solution:
    def reverse(self, t: List[str], f: Callable[[str], bool]) -> None:
        i, j = 0, len(t) - 1

        while i < j:

            while i < j and f(t[i]):
                i += 1
            
            while i < j and f(t[j]):
                j -= 1
            
            t[i], t[j] = t[j], t[i]
            i += 1
            j -= 1

    def reverseByType(self, s: str) -> str:
        t = list(s)
        self.reverse(t, str.islower)
        self.reverse(t, lambda ch: not ch.islower())
        
        return ''.join(t)