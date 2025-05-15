from typing import List
import bisect

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        # Create a list of (start, index) and sort by start
        sorted_starts = sorted((start, i) for i, (start, end) in enumerate(intervals))
        starts_only = [start for start, _ in sorted_starts]
        
        result = []
        for interval in intervals:
            end = interval[1]
            # Binary search for the smallest start >= current end
            # IDEA hay: tìm thằng start đầu tiên lớn hơn thằng end là được bằng binary search
            idx = bisect.bisect_left(starts_only, end)
            if idx < len(intervals):
                result.append(sorted_starts[idx][1])  # Return original index
            else:
                result.append(-1)
        return result
