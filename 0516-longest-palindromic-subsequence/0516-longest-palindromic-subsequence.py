class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]

        # Base case: every single letter is a palindrome of length 1
        for i in range(n):
            dp[i][i] = 1

        # Fill in order of increasing substring length
        for end in range(n):
            for start in range(end - 1, -1, -1):  # go backward to ensure dp[start + 1][end - 1] is ready
                if s[start] == s[end]:
                    if end - start == 1:
                        dp[start][end] = 2
                    else:
                        dp[start][end] = 2 + dp[start + 1][end - 1]
                else:
                    dp[start][end] = max(dp[start + 1][end], dp[start][end - 1])

        return dp[0][n - 1]
