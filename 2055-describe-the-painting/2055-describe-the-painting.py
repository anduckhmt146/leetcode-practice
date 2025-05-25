from typing import List
from collections import defaultdict

class Solution:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        changes = defaultdict(int)

        # Record color increments and decrements at segment boundaries
        for start, end, color in segments:
            changes[start] += color
            changes[end] -= color

        points = sorted(changes.keys())

        result = []
        curr_color = 0
        prev_point = points[0]

        for i in range(len(points)):
            point = points[i]

            if i > 0 and curr_color > 0:
                # Create segment from prev_point to current point
                result.append([prev_point, point, curr_color])

            # Update curr_color after recording the segment
            curr_color += changes[point]
            prev_point = point

        return result
