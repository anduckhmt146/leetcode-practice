class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        # Find 2D n x n
        n = len(values)
        dp = [[0] * n for _ in range(n)]

        for length in range(3, n + 1):
            for i in range(n - length + 1):
                # Sub range (i, j)
                j = i + length - 1
                dp[i][j] = float('inf')
                for k in range(i, j):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + values[i] * values[k] * values[j])

        return dp[0][n - 1]