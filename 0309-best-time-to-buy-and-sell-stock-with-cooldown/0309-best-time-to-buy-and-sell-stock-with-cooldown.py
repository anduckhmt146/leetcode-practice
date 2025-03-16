class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize variables:
        # freeze_profit (f) - profit of the day before cooldown
        # sell_profit (f0) - profit after selling the stock
        # hold_profit (f1) - profit after buying the stock or holding onto the stock bought previously
        freeze_profit, sell_profit, hold_profit = 0, 0, -prices[0]

        # Iterate through the stock prices, starting from the second day
        for current_price in prices[1:]:
            # Update profits for the current day
            # freeze_profit remains as the sell_profit from the previous day
            # sell_profit is the maximum of either keeping the previous sell_profit or selling stock today (hold_profit + current_price)
            # hold_profit is the max of either keeping the stock bought previously or buying new stock after cooldown (freeze_profit - current_price)
            freeze_profit, sell_profit, hold_profit = (
                sell_profit, 
                max(sell_profit, hold_profit + current_price),
                max(hold_profit, freeze_profit - current_price)
            )

        # The maximum profit will be after all trades are done, which means no stock is being held, hence sell_profit
        return sell_profit

        