from bisect import bisect_right

class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        # Sort by end_time
        rides.sort(key=lambda x:x[1]) # Sort by end_time
        m = len(rides)

        # Store the max_value in job i
        end_times = [ride[1] for ride in rides]
        dp = [0] * (m  + 1)

        # Start from i + 1 -> i
        for i in range(1, m + 1):
            start, end, tip = rides[i - 1]
            earning = end - start + tip

            idx = bisect_right(end_times, start, lo = 0, hi = i - 1)
            dp[i] = max(dp[i - 1], dp[idx] + earning)

        return dp[m]

