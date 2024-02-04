class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        if income<=brackets[0][0]:
            #make as much as or less than first bracket
            return min(brackets[0][0], income) * (brackets[0][1]/100)
        tax = (brackets[0][0]*brackets[0][1]/100)
        income = income - brackets[0][0]
        for i in range(1,len(brackets)):
            print(income)
            dollars = brackets[i][0] -brackets[i-1][0]
            rate = brackets[i][1]
            if income - dollars >=0:
                #Can pay all
                tax += dollars * (rate/100)
                income = income - dollars
            else:
                tax += (income)*(rate/100)
                break
        return tax

        