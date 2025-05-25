from typing import List

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        # Sort intervals by start ascending, and end descending
        intervals.sort(key=lambda x: (x[0], -x[1]))

        count = 0
        prev_end = 0

        for _, end in intervals:
            # If current end is greater than previous, it's not covered
            if end > prev_end:
                count += 1
                prev_end = end
            # else: current interval is covered

        return count
