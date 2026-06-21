class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegrees = [0] * numCourses
        adj = {i:[] for i in range(numCourses)}

        for x,y in prerequisites:
            adj[y].append(x)
            indegrees[x] += 1
        
        queue = deque([])
        for i in range(numCourses):
            if indegrees[i] == 0:
                queue.append(i)
        
        visited = 0
        while queue:
            curr = queue.popleft()
            visited += 1
            for n in adj[curr]:
                indegrees[n] -= 1
                if indegrees[n] == 0:
                    queue.append(n)
        return visited == numCourses
                    
