class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.

        """
        #Similarily to water flowing question, we want to start on the outside, and see if we can reach any O's from the border. IF we can, then it is safe.
        if not board:
            return 0
        rows, cols = len(board), len(board[0])
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        def dfs(r,c): #DFS to traverse and mark safe positions
            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != 'O':
                return
            board[r][c] = "S" #Safe!
            for x,y in directions:
                moved_row, moved_col = x+r, y+c
                if moved_row in range(rows) and moved_col in range(cols) and board[moved_row][moved_col] == "O":
                    dfs(moved_row, moved_col)


        for r in range(rows):
            for c in [0, cols - 1]:  # First and last column
                if board[r][c] == 'O':
                    dfs(r, c)
        for c in range(cols):
            for r in [0, rows - 1]:  # First and last row
                if board[r][c] == 'O':
                    dfs(r, c)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                if board[r][c] == "S":
                    board[r][c] = "O"
                    




        