class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, len(prices)-1
        min_p = prices[0]
        maxProfit = 0
        for p in prices:
            min_p = min(min_p,p)
            currentProfit = p-min_p
            if currentProfit >0:
                maxProfit = max(maxProfit, currentProfit)
        return maxProfit
            



        