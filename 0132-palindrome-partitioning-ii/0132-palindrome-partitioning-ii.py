class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        # pal[i][j] = True if s[i:j+1] is a palindrome
        pal = [[False] * n for _ in range(n)]

        for i in range(n):
            pal[i][i] = True  # single character is always a palindrome

        # Fill pal table
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    if length == 2 or pal[i + 1][j - 1]:
                        pal[i][j] = True

        # dp[i] = min cuts needed for s[0..i]
        dp = [0] * n
        for i in range(n):
            if pal[0][i]:
                dp[i] = 0
            else:
                dp[i] = float('inf')
                for j in range(i):
                    if pal[j + 1][i]:
                        dp[i] = min(dp[i], dp[j] + 1)

        return dp[n - 1]
