from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        # Sort intervals by end time
        intervals.sort(key=lambda x: x[1])
        
        count = 0
        prev_end = intervals[0][1]

        for i in range(1, len(intervals)):
            start, end = intervals[i]
            if start < prev_end:
                # Overlap found, need to remove one
                count += 1
            else:
                # No overlap, update prev_end
                prev_end = end

        return count
