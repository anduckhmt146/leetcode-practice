from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        n = len(prices)
        hold = -prices[0]     # Buy on day 0
        sold = 0              # Nothing sold yet
        rest = 0              # Initial rest state

        for price in prices[1:]:
            prev_hold = hold
            prev_sold = sold
            prev_rest = rest

            hold = max(prev_hold, prev_rest - price) # Buy
            sold = prev_hold + price                # Sell
            rest = max(prev_rest, prev_sold)        # Stay resting or go into cooldown 

        return max(sold, rest)  # Final profit must not be holding
