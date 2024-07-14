class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #some sort of 2d binary search
        ROWS, COLS = len(matrix), len(matrix[0])
        left, right = 0, (ROWS*COLS)-1
        while left <= right:
            total = (left + right)//2
            row = total // COLS
            col = total - (row*COLS)
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                # need to search lower
                right = total-1
            else:
                left = total+1
        return False



                
        

            

            



