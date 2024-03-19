class ATM:

    def __init__(self):
        self.banknotes = [0]*5
        self.values = [20,50,100,200,500]
        

    def deposit(self, banknotesCount: List[int]) -> None:
        for i in range(len(banknotesCount)):
            self.banknotes[i] +=banknotesCount[i]        

    def withdraw(self, amount: int) -> List[int]:
        withdraw = [0]*5
        for i in range(4,-1,-1):
            withdraw[i] = min(self.banknotes[i], amount // self.values[i])
            amount -=withdraw[i] * self.values[i]
        if amount ==0:
            #able to withdraw
            for i in range(5):
                self.banknotes[i] -= withdraw[i]
        return [-1] if amount !=0 else withdraw

        


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)