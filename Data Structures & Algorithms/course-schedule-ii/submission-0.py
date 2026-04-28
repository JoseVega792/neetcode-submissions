class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        graph = {i:[] for i in range(numCourses)}

        for x,y in prerequisites:
            graph[y].append(x)
            indegree[x] += 1
        
        queue = deque([])
        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)
        
        res = []
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                res.append(node)
                for c in graph[node]:
                    indegree[c] -= 1
                    if indegree[c] == 0:
                        queue.append(c)
        return res if len(res) == numCourses else []