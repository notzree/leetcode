class Solution:
    def generateParenthesis(self, n: int) -> List[str]:   
        stack = []
        ps = []
        def back(openP, closedP):
            if openP == closedP == n:
                ps.append("".join(stack))
            if openP < n:
                stack.append("(")
                back(openP+1, closedP)
                stack.pop()
            if openP > closedP and closedP < n:
                stack.append(")")
                back(openP, closedP+1)
                stack.pop()
        back(0,0)
        return ps

            
            








    
