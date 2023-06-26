class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1
        counter = 0
        while left <= right :
            if s[left] != s[right]:
                dLeft = s[left+1:right+1] #Go from left+1 to right inclusive
                dRight = s[left:right] # Go from left to right exclusive
                
                return dLeft == dLeft[::-1] or dRight == dRight [::-1]
            left = left +1
            right = right -1
        return True

