class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return ""

        dp = [[False] * n for _ in range(n)]
        start = 0
        max_len = 1

        for end in range(n):
            for i in range(end + 1):
                if s[i] == s[end]:
                    if end - i <= 2:
                        dp[i][end] = True
                    else:
                        dp[i][end] = dp[i + 1][end - 1]

                    if dp[i][end] and end - i + 1 > max_len:
                        start = i
                        max_len = end - i + 1

        return s[start:start + max_len]
