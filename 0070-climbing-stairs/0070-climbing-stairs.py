class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        # Use two variables to track dp[n-1] and dp[n-2]
        prev1, prev2 = 2, 1  # prev1 is dp[n-1] and prev2 is dp[n-2]
        
        for i in range(3, n + 1):
            current = prev1 + prev2
            prev2 = prev1
            prev1 = current
        
        return current
