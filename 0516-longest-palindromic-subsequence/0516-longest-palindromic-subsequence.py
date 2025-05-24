class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        # Create a 2D DP array initialized to 0
        dp = [[0] * n for _ in range(n)]

        # All substrings of length 1 are palindromes of length 1
        for i in range(n):
            dp[i][i] = 1

        # Build the DP table
        for length in range(2, n + 1):  # Substring lengths from 2 to n
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    dp[i][j] = 2 + dp[i + 1][j - 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        return dp[0][n - 1]
