import math

class Solution:
    def numSquares(self, n: int) -> int:
        # dp[i] will be the least number of perfect square numbers that sum to i
        dp = [float('inf')] * (n + 1)
        dp[0] = 0  # base case: 0 is made up of 0 numbers

        # Precompute all perfect squares less than or equal to n
        squares = [i * i for i in range(1, int(math.sqrt(n)) + 1)]

        for square in squares:
            for i in range(square, n + 1):
                dp[i] = min(dp[i], dp[i - square] + 1)

        return dp[n]
