class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        #bfs, if we can travel from a rotten orange to a good orange, then we mark it as rotten
        if not grid:
            return -1
        rows, cols = len(grid), len(grid[0])
        directions = [ [1,0], [-1,0], [0,1], [0,-1]]
        minutes = 0
        queue = []
        fresh = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r,c))
                if grid[r][c]==1:
                    fresh+=1 
        
        while queue and fresh > 0:
            minutes+=1
            for _ in range(len(queue)):
                (curr_row,curr_col) = queue.pop(0)
                for (row_inc, col_inc) in directions:
                    moved_row, moved_col = curr_row + row_inc, curr_col + col_inc
                    if moved_row in range(rows) and moved_col in range(cols) and grid[moved_row][moved_col]==1:
                        fresh -=1
                        grid[moved_row][moved_col] = 2
                        queue.append((moved_row, moved_col))

        return minutes if fresh ==0 else -1
        
        
        



            
        