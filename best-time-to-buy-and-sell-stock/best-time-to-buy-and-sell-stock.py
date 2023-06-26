class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minVal = prices[0]
        best = 0
        
        for p in range(1, len(prices)):
            minVal = min(minVal, prices[p])
            best = max(best, prices[p]-minVal)
        return best