from typing import List
from bisect import bisect_left, insort
from collections import defaultdict

class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        MOD = 10**9 + 7
        
        events = []
        for r in rectangles:
            # (x, type, y1, y2)
            events.append([r[0], 0, r[1], r[3]])  # opening edge
            events.append([r[2], 1, r[1], r[3]])  # closing edge
        
        # Sort by x, then by type (open before close)
        events.sort(key=lambda x: (x[0], x[1]))
        
        yline = []  # active intervals as (y, type): 1 = entry, -1 = exit
        prev_x = None
        area = 0

        def get_area(width):
            yline_sorted = sorted(yline)
            count = 0
            total_y = 0
            prev_y = None
            for y, typ in yline_sorted:
                if count == 0:
                    prev_y = y
                count += typ
                if count == 0 and prev_y is not None:
                    total_y += y - prev_y
            return total_y * width

        for x, typ, y1, y2 in events:
            if prev_x is not None:
                width = x - prev_x
                area = (area + get_area(width)) % MOD

            if typ == 0:
                # insert y1 (entry) and y2 (exit)
                yline.append((y1, 1))
                yline.append((y2, -1))
            else:
                # remove y1 (entry) and y2 (exit)
                yline.remove((y1, 1))
                yline.remove((y2, -1))

            prev_x = x

        return area
