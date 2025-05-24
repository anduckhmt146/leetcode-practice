from typing import List
import bisect

class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        # Sort rides by start time
        rides.sort(key=lambda x: x[0])
        starts = [ride[0] for ride in rides]

        memo = {}

        def knapsack(currIndex: int) -> int:
            # Base case
            if currIndex >= len(rides):
                return 0

            if currIndex in memo:
                return memo[currIndex]

            start, end, tip = rides[currIndex]
            earning = (end - start) + tip

            # Find next ride index that can be taken after this one
            nextIndex = bisect.bisect_left(starts, end)

            # Option 1: Include current ride + optimal from next compatible ride
            include = earning + knapsack(nextIndex)
            # Option 2: Skip current ride
            exclude = knapsack(currIndex + 1)

            memo[currIndex] = max(include, exclude)
            return memo[currIndex]

        return knapsack(0)
