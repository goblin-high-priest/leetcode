class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        binary_set = set()

        for i in range(len(s) - k + 1):
            sub = s[i:i+k]
            binary_set.add(sub)
        
        return True if len(binary_set) == 2 ** k else False