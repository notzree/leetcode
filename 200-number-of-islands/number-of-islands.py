class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        visited = set() #Or can use 2d grid
        islands = 0

        def bfs(r,c):
            #BFS is an iterative algo
            q = collections.deque()
            visited.add((r,c))
            q.append((r,c))
            while q:
                row, col = q.popleft()
                #check adj positions for position we just popped
                directions = [[1,0], [-1,0],[0,1], [0,-1]]
                for dr, dc in directions:
                    moved_row, moved_col = row+dr, col+dc
                    if (moved_row) in range(rows) and (moved_col) in range(cols) and grid[moved_row][moved_col]=="1" and (moved_row,moved_col) not in visited:
                        q.append((moved_row,moved_col))
                        visited.add((moved_row,moved_col))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    #Traverse and mark it visited
                    bfs(r,c)
                    islands+=1
        return islands

        
                    

        

        

        