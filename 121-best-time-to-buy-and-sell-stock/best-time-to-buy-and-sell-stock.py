class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyprice = prices[0]
        profit = 0

        for i in range(0, len(prices)):
            buyprice = min(buyprice, prices[i])
            profit = max(profit, prices[i]-buyprice)
        return profit
