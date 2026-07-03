class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        R, C = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()
        def dfs(r, c, prev, ocean):
            if r < 0 or r >= R or c < 0 or c >= C or (r,c) in ocean or heights[r][c] < prev:
                return 
            
            ocean.add((r,c))
            directions = [(-1,0), (1,0), (0,-1), (0,1)]
            for x,y in directions:
                newX, newY = x + r, y + c
                dfs(newX, newY, heights[r][c], ocean)
        
        # Top - Bottom
        for i in range(C):
            dfs(0,i, heights[0][i], pacific)
            dfs(R - 1, i, heights[R-1][i],atlantic)
        # Left - Right
        for i in range(R):
            dfs(i,0,heights[i][0],pacific)
            dfs(i,C-1, heights[i][C-1], atlantic)
        res = []
        for r in range(R):
            for c in range(C):
                if (r,c) in pacific and (r,c) in atlantic:
                    res.append([r,c])
        return res