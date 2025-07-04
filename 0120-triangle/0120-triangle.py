class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return 0

        # Start from the bottom row
        dp = triangle[-1][:]  # Copy the last row

        # Iterate from the second-to-last row upward
        for row in range(len(triangle) - 2, -1, -1):
            for col in range(len(triangle[row])):
                # Update dp[col] to be the min path sum from this cell
                dp[col] = triangle[row][col] + min(dp[col], dp[col + 1])

        return dp[0]  # Top element will contain the minimum path sum
