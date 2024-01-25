class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        width = len(board)
        height = len(board[0])
        visited = set()
        def solve(row, col, i):
            if i==len(word):
                return True
            if i >len(word):
                return False
            if row >= width or col >= height or row < 0 or col < 0 or board[row][col]!=word[i] or (row,col) in visited:
                return False
            visited.add((row,col))
            res = solve(row+1, col, i+1) or solve(row-1, col, i+1) or solve(row, col+1, i+1) or  solve(row, col-1, i+1)
            visited.remove((row,col))
            return res
        for w in range(width):
            for h in range(height):
                if solve(w,h,0): return True

            
            
        