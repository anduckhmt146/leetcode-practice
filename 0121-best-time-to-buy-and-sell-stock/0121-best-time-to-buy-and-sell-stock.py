from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0
        
        dp0 = 0             # Max profit without stock
        dp1 = -prices[0]    # Max profit with one stock bought
        
        for i in range(1, n):
            dp0 = max(dp0, dp1 + prices[i])  # Sell today or do nothing
            dp1 = max(dp1, -prices[i])       # Buy today or do nothing
        
        return dp0
