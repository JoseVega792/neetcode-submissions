class Solution:

    def bfs(self, grid, r, c):
        res = 1
        queue = deque([(r,c)])
        grid[r][c] = 0
        while queue:
            for _ in range(len(queue)):
                x,y = queue.popleft()
                for i,j in [(1,0), (-1,0), (0,1), (0,-1)]:
                    newX, newY = x + i, j + y
                    if 0 <= newX < len(grid) and 0 <= newY < len(grid[newX]) and grid[newX][newY] == 1:
                        res += 1
                        grid[newX][newY] = 0
                        queue.append((newX, newY))
        return res

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 1:
                    res = max(res, self.bfs(grid, r, c))
        return res