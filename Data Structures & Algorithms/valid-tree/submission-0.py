class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n - 1:
            return False
        
        adj = {i:[] for i in range(n)}
        for x,y in edges:
            adj[x].append(y)
            adj[y].append(x)
        
        seen = set()
        queue = deque([(0,-1)])
        seen.add(0)

        while queue:
            node, parent = queue.popleft()
            for nei in adj[node]:
                if nei == parent:
                    continue
                if nei in seen:
                    return False
                seen.add(nei)
                queue.append((nei,node))
        return len(seen) == n