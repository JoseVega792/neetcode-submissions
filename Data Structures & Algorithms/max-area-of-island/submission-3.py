class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(0,1), (1,0), (-1, 0), (0,-1)]
        seen = set()
        maxArea = 0
        def bfs(x,y):
            queue = deque([(x,y)])
            seen.add((x,y))
            currArea = 0
            while queue:
                currArea += 1
                currX, currY = queue.popleft()
                for i,j in directions:
                    newX = currX + i
                    newY = currY + j
                    if newX >= 0 and newX < len(grid) and newY >= 0  and newY < len(grid[x]) and (newX, newY) not in seen and grid[newX][newY] == 1:
                        seen.add((newX,newY))
                        queue.append((newX,newY))
            return currArea
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (i,j) not in seen and grid[i][j] == 1:
                    maxArea = max(maxArea, bfs(i,j))
        return maxArea
