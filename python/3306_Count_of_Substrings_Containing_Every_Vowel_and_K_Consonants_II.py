class Solution:
    def at_least_k_consonant(self, word: str, k: int) -> int:
        cnt_vowel = defaultdict(int)
        cnt_consonant = 0
        res = 0

        left = 0
        for c in word:

            if c in "aeiou":
                cnt_vowel[c] += 1
            else:
                cnt_consonant += 1

            while len(cnt_vowel) == 5 and cnt_consonant >= k:
                out = word[left]

                if out in "aeiou":
                    cnt_vowel[out] -= 1

                    if cnt_vowel[out] == 0:
                        del cnt_vowel[out]
                else:
                    cnt_consonant -= 1
                
                left += 1
            res += left

        return res
            
    def countOfSubstrings(self, word: str, k: int) -> int:
        return self.at_least_k_consonant(word, k) - self.at_least_k_consonant(word, k + 1)
        