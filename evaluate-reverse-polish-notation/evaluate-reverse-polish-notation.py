class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for i in tokens:
            if i not in "+-*/":
                s.append(int(i))
            else: #i is an operator.
                t2 = s.pop() #second number
                t1 = s.pop()
            # first num is s.pop()
                if i == "+":
                    s.append(t1+t2)
                elif i == "-":
                    s.append(t1-t2)
                elif i == "*":
                    s.append(t1*t2)
                else:
                    s.append(int(float(t1)/t2))
        return s.pop()




