class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(x,y,prev, ocean):
            if x < 0 or x >= ROWS or y < 0 or y >= COLS or (x,y) in ocean or heights[x][y] < prev:
                return
            ocean.add((x,y))
            directions = [(-1,0),(1,0),(0,1),(0,-1)]
            for r,c in directions:
                nx = x + r
                ny = c + y
                dfs(nx,ny,heights[x][y],ocean)
        
        for r in range(ROWS):
            dfs(r,0,heights[r][0],pac)
            dfs(r,COLS-1, heights[r][COLS-1], atl)
        
        for c in range(COLS):
            dfs(0,c, heights[0][c], pac)
            dfs(ROWS-1, c, heights[ROWS-1][c], atl)
        
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r,c) in atl:
                    res.append([r,c])
        return res