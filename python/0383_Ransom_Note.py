class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        if len(ransomNote) > len(magazine):
            return False
        
        magazine_counts = Counter(magazine)

        for c in ransomNote:

            if magazine_counts[c] == 0:
                return False
            
            magazine_counts[c] -= 1
        
        return True