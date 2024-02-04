class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        digitToChar = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"prqs",
            "8":"tuv",
            "9":"wxyz"
        }
        combination = []
        for c in digitToChar[digits[0]]:
            combination.append(c)
        if len(digits)==1:
            return combination
        for d in digits[1:]:
            for c in range(len(combination)):
                curr = combination.pop(0)
                for letter in digitToChar[d]:
                    combination.append(curr+letter)
        return combination
            
        