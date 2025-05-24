from typing import List
import bisect

class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        # Sort rides by end time
        rides.sort(key=lambda x: x[1])
        # dp[i] will store the max earnings up to the i-th ride
        dp = [0] * (len(rides) + 1)
        # end_times will store the end time of each ride for binary search
        end_times = [ride[1] for ride in rides]

        for i in range(1, len(rides) + 1):
            start, end, tip = rides[i - 1]
            earning = end - start + tip
            # Find the last ride that ends before the current ride starts
            j = bisect.bisect_right(end_times, start)  # gives index of first end_time > start
            dp[i] = max(dp[i - 1], dp[j] + earning)

        return dp[-1]
