class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0

        for i in range(0, len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            
            # profit = price[i] - min_price at previous time
            max_profit = max(max_profit, prices[i] - min_price)
        
        return max_profit