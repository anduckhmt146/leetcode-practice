from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')  # Initialize to a very high value
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price  # Update minimum price
            else:
                max_profit = max(max_profit, price - min_price)  # Potential profit

        return max_profit
