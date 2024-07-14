class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #some sort of 2d binary search
        ROWS, COLS = len(matrix), len(matrix[0])

        top, bot = 0, ROWS-1
        while top <= bot:
            row = (top+bot)//2
            if target > matrix[row][-1]: # Need to search closer to bot
                top = row+1
            elif target < matrix[row][0]: # Need to search closer to top
                bot = row -1
            else:
                break
        if not (top<=bot): return False
        row = (top+bot)//2
        left, right = 0, COLS-1
        while left <=right:
            col = (left + right) //2
            if matrix[row][col] == target:
                return True
            elif target > matrix[row][col]: # Need check smaller half
                left = col+1
            else:
                right = col-1
        return False
                
        

            

            



