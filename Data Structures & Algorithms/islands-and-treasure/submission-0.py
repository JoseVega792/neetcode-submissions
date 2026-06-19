class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        directions = [(-1,0), (1,0), (0,1), (0, -1)]
        queue = deque([])
        dist = 0
        INF = 2147483647
        #Find Chest
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    queue.append((i,j))
        #Update grid based on location
        while queue:
            dist += 1
            for _ in range(len(queue)):
                currX, currY = queue.popleft()
                for x,y in directions:
                    newX = x + currX
                    newY = y + currY
                    if newX < 0 or newX >= len(grid) or newY < 0 or newY >= len(grid[newX]) or grid[newX][newY] != INF:
                        continue
                    grid[newX][newY] = dist
                    queue.append((newX, newY))