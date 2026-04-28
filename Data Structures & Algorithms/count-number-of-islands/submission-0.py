class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0

        def dfs(r,c,grid):
            if grid[r][c] == '0':
                return
            grid[r][c] = '0'
            for x,y in [(-1,0),(1,0),(0,1),(0,-1)]:
                newR, newC = x + r, c + y
                if 0 <= newR < len(grid) and 0 <= newC < len(grid[0]) and grid[newR][newC] == '1':
                    dfs(newR,newC,grid)
            return
        
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == '1':
                    res += 1
                    dfs(r,c,grid)
        return res