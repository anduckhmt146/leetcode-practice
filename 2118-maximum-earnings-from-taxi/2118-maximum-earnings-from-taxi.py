from typing import List
import bisect

class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        # Sort rides by their end time
        rides.sort(key=lambda x: x[1])

        # Extract start and end times for binary searching
        starts = [ride[0] for ride in rides]
        ends = [ride[1] for ride in rides]

        m = len(rides)
        # dp[i] means max earnings considering rides up to i-th ride (1-indexed)
        dp = [0] * (m + 1)

        for i in range(1, m + 1):
            start, end, tip = rides[i - 1]
            earning = end - start + tip

            # Find index of the last ride that ends before current ride starts
            # We want the max dp[j] where rides[j-1].end <= start
            idx = bisect.bisect_right(ends, start)  # rides ending <= start
            # idx is the count of rides that end before 'start', dp is 1-indexed, so dp[idx] valid

            # max of excluding current ride or including current ride + best before idx
            dp[i] = max(dp[i - 1], earning + dp[idx])

        return dp[m]
