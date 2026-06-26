class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        indegrees = [0] * (n + 1)
        adj = {i: [] for i in range(n + 1)}
        for x,y in edges:
            indegrees[x] += 1
            indegrees[y] += 1
            adj[x].append(y)
            adj[y].append(x)
        
        queue = deque()
        for n in range(n + 1):
            if indegrees[n] == 1:
                queue.append(n)
        
        while queue:
            curr = queue.popleft()
            indegrees[curr] -= 1
            for nei in adj[curr]:
                indegrees[nei] -= 1
                if indegrees[nei] == 1:
                    queue.append(nei)
        
        for x,y in reversed(edges):
            if indegrees[x] == 2 and indegrees[y]:
                return [x,y]
        return []