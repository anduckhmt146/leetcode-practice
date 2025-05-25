from typing import List

class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        max_range = [0] * (n + 1)

        # Convert to [start, end] intervals and track max reach from each start
        for i in range(n + 1):
            left = max(0, i - ranges[i])
            right = min(n, i + ranges[i])
            max_range[left] = max(max_range[left], right)

        taps = 0
        curr_end = 0
        next_end = 0

        for i in range(n + 1):
            if i > next_end:
                return -1  # Cannot reach this point
            if i > curr_end:
                taps += 1
                curr_end = next_end
            next_end = max(next_end, max_range[i])

        return taps
