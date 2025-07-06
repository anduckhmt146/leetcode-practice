class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m, n = len(str1), len(str2)

        # Step 1: Find the LCS
        dp = [[""] * (n + 1) for _ in range(m + 1)]

        for i in range(m):
            for j in range(n):
                if str1[i] == str2[j]:
                    dp[i + 1][j + 1] = dp[i][j] + str1[i]
                else:
                    dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1], key=len)

        lcs = dp[m][n]

        # Step 2: Build the SCS using LCS
        res = []
        i = j = 0
        for c in lcs:
            while str1[i] != c:
                res.append(str1[i])
                i += 1
            while str2[j] != c:
                res.append(str2[j])
                j += 1
            res.append(c)
            i += 1
            j += 1

        # Add remaining parts
        res.append(str1[i:])
        res.append(str2[j:])

        return ''.join(res)
