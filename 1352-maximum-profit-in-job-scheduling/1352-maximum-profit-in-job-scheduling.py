from typing import List
import bisect

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # Combine all jobs into a list of tuples and sort by end time
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        
        # dp will store pairs of (endTime, maxProfitUntilThatTime)
        dp = [(0, 0)]  # base case: at time 0, profit is 0
        
        for s, e, p in jobs:
            # Use binary search to find the latest job that ends before the current job starts
            i = bisect.bisect_right(dp, (s, float('inf'))) - 1
            # Calculate new profit if this job is included
            curr_profit = dp[i][1] + p
            # Only add to dp if it's better than the last recorded profit
            if curr_profit > dp[-1][1]:
                dp.append((e, curr_profit))
        
        return dp[-1][1]
