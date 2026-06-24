class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        indegree = [0] * (n + 1)
        adj = {i:[] for i in range(n + 1)}
        for x,y in edges:
            adj[x].append(y)
            adj[y].append(x)
            indegree[x] += 1
            indegree[y] += 1
        
        queue = deque()
        for i in range(n + 1):
            if indegree[i] == 1:
                queue.append(i)
        
        while queue:
            curr = queue.popleft()
            indegree[curr] -= 1
            for nei in adj[curr]:
                indegree[nei] -= 1
                if indegree[nei] == 1:
                    queue.append(nei)
        
        for x,y in reversed(edges):
            if indegree[x] == 2 and indegree[y]:
                return [x,y]
        return []
