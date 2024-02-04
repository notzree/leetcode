class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        visited = set() #Or can use 2d grid
        islands = 0
        directions = [[1,0], [-1,0], [0,1], [0,-1]]

        def dfs(r,c):
            if r not in range(rows) or c not in range(cols) or (r,c) in visited or grid[r][c]=="0":
                return
            visited.add((r,c))
            for (row_inc,c_inc) in directions:
                moved_row,moved_col = r+row_inc, c+c_inc
                dfs(moved_row,moved_col)

            
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    #Traverse and mark it visited
                    dfs(r,c)
                    islands+=1
        return islands

        
                    

        

        

        