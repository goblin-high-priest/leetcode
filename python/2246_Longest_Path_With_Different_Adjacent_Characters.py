class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        res = [0]
        n = len(parent)
        par_to_child = defaultdict(list)

        for i in range(1, n):
            par_to_child[parent[i]].append(i)
        
        def dfs(root):
            max_len = 0

            for child in par_to_child[root]:
                cur_len = dfs(child) + 1

                if s[root] != s[child]:
                    res[0] = max(res[0], cur_len + max_len)
                    max_len = max(cur_len, max_len)
                
            return max_len
        
        dfs(0)

        return res[0] + 1
