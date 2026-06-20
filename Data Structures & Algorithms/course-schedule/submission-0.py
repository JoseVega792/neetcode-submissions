class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegrees = [0] * numCourses
        graph = {i:[] for i in range(numCourses)}

        for x,y in prerequisites:
            graph[y].append(x)
            indegrees[x] += 1
        
        queue = deque([])
        for i in range(numCourses):
            if indegrees[i] == 0:
                queue.append(i)
        
        visited = 0
        while queue:
            node = queue.popleft()
            visited += 1
            for n in graph[node]:
                indegrees[n] -= 1
                if indegrees[n] == 0:
                    queue.append(n)
        return visited == numCourses