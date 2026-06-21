class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegrees = [0] * numCourses
        adj = {i:[] for i in range(numCourses)}

        for x,y in prerequisites:
            adj[y].append(x)
            indegrees[x] += 1
        
        res = []
        queue = deque([])
        for i in range(numCourses):
            if indegrees[i] == 0:
                queue.append(i)
                res.append(i)
        
        visited = 0
        while queue:
            visited += 1
            curr = queue.popleft()
            res.append(curr)
            for n in adj[curr]:
                indegrees[n] -= 1
                if indegrees[n] == 0:
                    queue.append(n)
        return res if visited == numCourses else []