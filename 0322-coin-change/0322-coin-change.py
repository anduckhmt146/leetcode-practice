from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dp(rem: int) -> int:
            # Base case: if amount is 0, we need 0 coins
            if rem == 0:
                return 0
            # If amount becomes negative, no solution
            if rem < 0:
                return float('inf')
            # If already computed, return cached result
            if rem in memo:
                return memo[rem]

            # Try every coin and choose the best (min)
            min_coins = float('inf')
            for coin in coins:
                res = dp(rem - coin)
                if res != float('inf'):
                    min_coins = min(min_coins, res + 1)

            memo[rem] = min_coins
            return min_coins

        result = dp(amount)
        return result if result != float('inf') else -1
