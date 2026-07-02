class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = {i:[] for i in range(len(edges) + 1)}
        indegrees = [0] * (len(edges) + 1)
        
        for x,y in edges:
            indegrees[x] += 1
            indegrees[y] += 1
            adj[x].append(y)
            adj[y].append(x)
        
        q = deque([])
        for i,num in enumerate(indegrees):
            if num == 1:
                q.append(i)
        
        while q:
            curr = q.popleft()
            indegrees[curr] -= 1
            for nei in adj[curr]:
                indegrees[nei] -= 1
                if indegrees[nei] == 1:
                    q.append(nei)
        
        for x,y in reversed(edges):
            if indegrees[x] == 2 and indegrees[y]:
                return [x,y]
        return []