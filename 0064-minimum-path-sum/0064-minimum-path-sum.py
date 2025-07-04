class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])

        dp = [[0] * col for _ in range(row)]

        # Init dp
        dp[0][0] = grid[0][0]

        # We can do it because we start from (0, 0)
        # Start first row
        for j in range(1, col):
            dp[0][j] = grid[0][j] + dp[0][j - 1] 

        # Start left column
        for i in range(1, row):
            dp[i][0] = grid[i][0] + dp[i - 1][0]


        # Fill in another value
        for i in range(1, row):
            for j in range(1, col):
                dp[i][j] = grid[i][j] + min(dp[i - 1][j], dp[i][j - 1])

        return dp[row - 1][col - 1]