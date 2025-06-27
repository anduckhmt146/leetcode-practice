from bisect import bisect_right

class Solution:
    def jobScheduling(self, startTime, endTime, profit):
        # Combine all job info
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])  # sort by endTime
        n = len(jobs)

        # dp[i]: max profit until taking to first i jobs
        dp = [0] * (n + 1)
        end_times = [job[1] for job in jobs]

        for i in range(1, n + 1):
            s, e, p = jobs[i - 1]
            
            # Find the last job that ends before this one starts
            idx = bisect_right(end_times, s, lo=0, hi=i-1)  # binary search
            dp[i] = max(dp[i - 1], dp[idx] + p)

        return dp[n]
