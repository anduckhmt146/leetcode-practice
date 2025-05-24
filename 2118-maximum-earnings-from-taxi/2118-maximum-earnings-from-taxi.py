from typing import List
import bisect

class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        # Sort rides by end time (important for bottom-up)
        rides.sort(key=lambda x: x[1])
        
        # Extract starts and ends separately for binary search
        starts = [ride[0] for ride in rides]
        ends = [ride[1] for ride in rides]

        dp = [0] * (len(rides) + 1)  # dp[i] = max earnings considering rides up to i-th (1-indexed)
        
        for i in range(1, len(rides) + 1):
            start, end, tip = rides[i - 1]
            earning = end - start + tip
            
            # Find last ride that ends before this ride starts (non-overlapping)
            # We want ride with end <= start, so binary search on ends for start
            # bisect_right gives insertion pos, subtract 1 for index of last non-overlapping ride
            idx = bisect.bisect_right(ends, start)  
            
            # dp[i] is max of:
            # 1) skip current ride: dp[i-1]
            # 2) take current ride: earning + dp[idx]
            dp[i] = max(dp[i-1], earning + dp[idx])
        
        return dp[-1]
