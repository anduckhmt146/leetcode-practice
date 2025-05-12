class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        # Sort intervals based on the start time
        intervals += [newInterval]

        if len(intervals) < 2:
            return intervals

        intervals.sort(key=lambda x: x[0])

        merged = []
        start, end = intervals[0]

        for i in range(1, len(intervals)):
            curr_start, curr_end = intervals[i]

            if curr_start <= end:  # Overlapping intervals
                end = max(end, curr_end)
            else:
                # Non-overlapping interval, append previous one
                merged.append([start, end])
                start, end = curr_start, curr_end

        # Add the last interval
        merged.append([start, end])

        return merged
        