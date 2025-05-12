from typing import List

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        # Step 1: Merge both lists
        intervals = firstList + secondList
        
        # Step 2: Sort by start time
        intervals.sort(key=lambda x: x[0])
        
        result = []
        prev = intervals[0]

        for i in range(1, len(intervals)):
            curr = intervals[i]

            # Check for overlap
            start = max(prev[0], curr[0])
            end = min(prev[1], curr[1])
            if start <= end:
                result.append([start, end])

            # Update prev to the one that extends further
            if curr[1] > prev[1]:
                prev = curr

        return result
