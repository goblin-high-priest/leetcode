class Solution:
    def count_vowel(self, s: str) -> int:
        return sum(c in "aeiou" for c in s)

    def reverseWords(self, s: str) -> str:
        words = s.split()

        for i in range(1, len(words)):
            cnt = self.count_vowel(words[0])

            if self.count_vowel(words[i]) == cnt:
                words[i] = words[i][::-1]
            
        return ' '.join(words)