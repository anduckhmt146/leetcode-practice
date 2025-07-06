from typing import List

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if not prices:
            return 0

        cash = 0
        hold = -prices[0]  # Buy on day 0

        for price in prices[1:]:
            cash = max(cash, hold + price - fee)  # Sell
            hold = max(hold, cash - price)        # Buy

        return cash
