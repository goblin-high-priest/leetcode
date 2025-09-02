class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        res = []
        
        for s in strs:
            res.append(str(len(s)))
            res.append('#')
            res.append(s)
        
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        res = []
        start = end = 0

        while end < len(s):
            start = s.find('#', end)
            length = int(s[end:start])
            end = start+1+length
            res.append(s[start+1:end])
        
        return res
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))