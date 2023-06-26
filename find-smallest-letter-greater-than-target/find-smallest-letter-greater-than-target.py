class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        n = ord(target)

        for i in letters:
            if ord(i) > n:
                return i
        return letters[0]
           
                
            


        
