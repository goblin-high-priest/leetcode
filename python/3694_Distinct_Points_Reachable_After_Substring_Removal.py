DIRS = {
    'L': (-1, 0),
    'R': (1, 0),
    'D': (0, -1),
    'U': (0, 1),
}
class Solution:
    def distinctPoints(self, s: str, k: int) -> int:
        st = set()
        x = y = 0

        for i, c in enumerate(s):
            dx, dy = DIRS[c]
            x += dx
            y += dy

            left = i + 1 - k

            if left < 0: continue

            st.add((x, y))

            dx, dy = DIRS[s[left]]
            x -= dx
            y -= dy
        
        return len(st)