class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        minStock, maxProfit = float('inf'), 0
        i = 0
        while (i < n):
            minStock = min(minStock, prices[i]) #ensures minimum stick is taken from start, no values repeated
            maxProfit = max(maxProfit, prices[i] - minStock) #ensures maximum profit is taken from start, no values repeated
            i += 1
        return maxProfit
