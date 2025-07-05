class Solution:
    def soupServings(self, n: int) -> float:
        if n >= 5000:
            return 1.0

        N = (n + 24) // 25
        dp = [[0.0 for _ in range(N + 1)] for _ in range(N + 1)]

        # Base cases
        for i in range(N + 1):
            dp[0][i] = 1.0          # A empty first
            dp[i][0] = 0.0          # B empty first
        dp[0][0] = 0.5              # Both empty at same time

        for a in range(1, N + 1):
            for b in range(1, N + 1):
                dp[a][b] = 0.25 * (
                    dp[max(0, a - 4)][b] +
                    dp[max(0, a - 3)][max(0, b - 1)] +
                    dp[max(0, a - 2)][max(0, b - 2)] +
                    dp[max(0, a - 1)][max(0, b - 3)]
                )

        return dp[N][N]
