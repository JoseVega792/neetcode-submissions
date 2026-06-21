class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # Obtain our O edges
        directions = [(-1,0),(1,0), (0,-1), (0,1)]
        ROWS, COLS = len(board), len(board[0])
        queue = deque([])
        for i in range(ROWS):
            if board[i][0] == "O":
                queue.append((i,0))
            if board[i][COLS - 1] == "O":
                queue.append((i, COLS - 1))

        for c in range(COLS):
            if board[0][c] == 'O':
                queue.append((0,c))
            if board[ROWS - 1][c] == "O":
                queue.append((ROWS - 1,c))
                
        #bfs out change the letters to Y's
        while queue:
            x,y = queue.popleft()
            board[x][y] = "Y"
            for i,j in directions:
                nx = i + x
                ny = y + j
                if 0 <= nx < ROWS and 0 <= ny < COLS and board[nx][ny] == "O":
                    queue.append((nx,ny))
        # modify our Os to Xs and Ys to Os
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "Y":
                    board[i][j] = "O"
        