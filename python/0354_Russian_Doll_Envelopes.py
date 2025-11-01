class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        g = []

        for i, e in enumerate(envelopes):
            h = e[1]
            j = bisect_left(g, h)

            if j == len(g):
                g.append(h)
            else:
                g[j] = h
            
        return len(g)
