class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        if n == 1:
            return [0]

        adjacency = defaultdict(list)
        edge_count = Counter()
        leaves = deque()
        
        for a, b in edges:
            adjacency[a].append(b)
            adjacency[b].append(a)
        
        for src, nei in adjacency.items():
            degree = len(nei)
            edge_count[src] = degree

            if degree == 1:
                leaves.append(src)
            
        while leaves:

            if n <= 2:
                return list(leaves)
            
            for _ in range(len(leaves)):
                node = leaves.popleft()
                n -= 1

                for nei in adjacency[node]:
                    edge_count[nei] -= 1

                    if edge_count[nei] == 1:
                        leaves.append(nei)
