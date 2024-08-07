class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(row: int, col: int, index: int):
            if row not in range(len(board)) or col not in range(len(board[0])) or board[row][col] !=word[index]:
                return False
            if index == len(word)-1:
                return True
            temp = board[row][col]
            board[row][col] = "#"
            for x_incr, y_incr in directions:
                new_row = row+y_incr
                new_col = col+x_incr
                if dfs(new_row, new_col, index+1):
                    return True
            board[row][col] = temp
            return False

        directions = [(0,1), (1,0), (0, -1), (-1,0)]
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == word[0]:
                    if dfs(r,c,0):
                        return True
        return False

            
            
        