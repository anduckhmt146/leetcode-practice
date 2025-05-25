from typing import List

class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        corner_set = set()
        total_area = 0

        min_x = float('inf')
        min_y = float('inf')
        max_x = float('-inf')
        max_y = float('-inf')

        for x1, y1, x2, y2 in rectangles:
            # Update bounding box
            min_x = min(min_x, x1)
            min_y = min(min_y, y1)
            max_x = max(max_x, x2)
            max_y = max(max_y, y2)

            # Accumulate area
            total_area += (x2 - x1) * (y2 - y1)

            # Define all four corners
            corners = [(x1, y1), (x1, y2), (x2, y1), (x2, y2)]

            # Use a set to track corners
            for c in corners:
                if c in corner_set:
                    corner_set.remove(c)
                else:
                    corner_set.add(c)

        # Final bounding rectangle area
        expected_area = (max_x - min_x) * (max_y - min_y)
        if total_area != expected_area:
            return False

        # Check corners — must match the 4 corners of bounding rectangle
        expected_corners = {(min_x, min_y), (min_x, max_y), (max_x, min_y), (max_x, max_y)}
        return corner_set == expected_corners
