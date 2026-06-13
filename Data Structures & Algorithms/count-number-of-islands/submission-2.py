class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(0,1), (0,-1), (1, 0), (-1,0)]
        res = 0
        def bfs(i,j):
            queue = deque([(i,j)])
            while queue:
                currX, currY = queue.popleft()
                grid[currX][currY] = "0"
                for x,y in directions:
                    newX = x + currX
                    newY = y + currY
                    if newX < 0 or newY < 0 or newX >= len(grid) or newY >= len(grid[0]):
                        continue
                    if grid[newX][newY] == "1":
                        queue.append((newX, newY))
            return 1
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    res += bfs(i,j)
        return res