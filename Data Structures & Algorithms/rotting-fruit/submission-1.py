class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [(-1,0), (1,0), (0,1), (0,-1)]
        freshCount = 0
        time = 0
        queue = deque([])
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    freshCount += 1
                if grid[i][j] == 2:
                    queue.append((i,j))
        
        while queue:
            time += 1
            for _ in range(len(queue)):
                x,y = queue.popleft()
                for i,j in directions:
                    newX = x + i
                    newY = y + j
                    if newX < 0 or newX >= len(grid) or newY < 0 or newY >= len(grid[newX]) or grid[newX][newY] != 1:
                        continue
                    freshCount -= 1
                    grid[newX][newY] = 2
                    queue.append((newX, newY))
        if time > 0:
            time -= 1
        return time if freshCount == 0 else -1
