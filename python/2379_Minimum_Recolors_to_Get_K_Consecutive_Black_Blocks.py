class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        left = 0
        res = inf

        cur = 0
        for right, c in enumerate(blocks):
            
            if c == 'W': cur += 1

            left = right - k + 1

            if left < 0: continue

            res = min(res, cur)
            
            if blocks[left] == 'W': cur -= 1
        
        return res