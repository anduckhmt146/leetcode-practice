class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)

        # dp[i][j] = number of distinct subsequences of s[0..i-1] that match t[0..j-1]
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # An empty t can always be matched by deleting all characters in s
        for i in range(m + 1):
            dp[i][0] = 1

        # Fill the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]:
                    # Match or skip s[i-1]
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    # Skip s[i-1]
                    dp[i][j] = dp[i - 1][j]

        return dp[m][n]
