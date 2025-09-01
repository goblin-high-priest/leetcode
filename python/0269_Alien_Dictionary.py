class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adj = {c: set() for word in words for c in word}

        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i+1]
            minLen = min(len(word1), len(word2))

            if len(word1) > len(word2) and word1[:minLen] == word2[:minLen]:
                return ""
            
            for j in range(minLen):
                
                if word1[j] != word2[j]:
                    adj[word1[j]].add(word2[j])
                    break
            
        visited = {}
        res = []

        def cycle_detection(c):
            
            if c in visited:
                return visited[c]
            
            visited[c] = True

            for neighbor in adj[c]:

                if cycle_detection(neighbor):
                    return True
            
            visited[c] = False
            res.append(c)
        
        for c in adj:

            if cycle_detection(c):
                return ""
        
        res.reverse()

        return "".join(res)