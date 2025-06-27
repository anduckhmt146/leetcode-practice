class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        rides.sort(key=lambda x: x[1])
        m = len(rides)

        # Extract end times for binary search
        end_times = [ride[1] for ride in rides]
        dp = [0] * (m + 1)

        for i in range(1, m + 1):
            start, end, tip = rides[i - 1]
            earnings = end - start + tip

            # Find the last ride that ends <= current ride's start
            idx = bisect_right(end_times, start, lo=0, hi=i - 1)
            # Two choices: take current ride or skip
            dp[i] = max(dp[i - 1], dp[idx] + earnings)

        return dp[m]
        