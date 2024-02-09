class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        pos_diagonals = set()
        neg_diagonals = set()
        cols = set()
        res = []
        board = [["."] * n for i in range(n)]


        def dfs(r):
            if r == n:
                #we found a valid soln
                copy = [ "".join(row) for row in board]
                res.append(copy)
                return
            for c in range(n):
                if c in cols or (r+c) in pos_diagonals or (r-c) in neg_diagonals:
                    continue
                cols.add(c)
                pos_diagonals.add(r+c)
                neg_diagonals.add(r-c)
                board[r][c] = "Q"
                dfs(r+1)
                board[r][c] = "."
                neg_diagonals.remove(r-c)
                pos_diagonals.remove(r+c)
                cols.remove(c)
        dfs(0)
        return res





        