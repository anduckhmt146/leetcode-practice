from typing import List

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        day_set = set(days)
        last_day = days[-1]
        dp = [0] * (last_day + 1)

        for day in range(1, last_day + 1):
            if day not in day_set:
                dp[day] = dp[day - 1]  # no travel, cost stays the same
            else:
                dp[day] = min(
                    dp[max(0, day - 1)] + costs[0],  # 1-day ticket
                    dp[max(0, day - 7)] + costs[1],  # 7-day ticket
                    dp[max(0, day - 30)] + costs[2]  # 30-day ticket
                )
        return dp[last_day]
