from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 0
        max_p = 0
        while sell < len(prices):
            if prices[buy] < prices[sell]:
                max_p = max(max_p, prices[sell] - prices[buy])
            else:
                buy = sell
            sell += 1
        return max_p