class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
    
    def addWord(self, word):
        cur = self

        for c in word:

            if c not in cur.children:
                cur.children[c] = TrieNode()
            
            cur = cur.children[c]
        
        cur.endOfWord = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        for word in words:
            root.addWord(word)
        
        ROWS, COLS = len(board), len(board[0])
        res, visited = set(), set()

        def dfs(r, c, node, word):

            if not 0 <= r < ROWS \
                or not 0 <= c < COLS \
                or (r, c) in visited \
                or board[r][c] not in node.children:
                return
            
            visited.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]

            if node.endOfWord:
                res.add(word)
            
            for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                dfs(r + dx, c + dy, node, word)

            visited.remove((r, c))
        
        for r in range(ROWS):
            for c in range(COLS):

                dfs(r, c, root, "")
        
        return list(res)
