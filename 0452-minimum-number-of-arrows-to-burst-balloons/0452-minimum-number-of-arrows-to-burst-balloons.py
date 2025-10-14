class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        # sort by interval end
        points.sort(key=lambda x: x[1])
        arrows = 1
        arrow_pos = points[0][1]  # shoot at end of first interval
        for s, e in points[1:]:
            if s <= arrow_pos <= e:
                # this interval is already burst by the last arrow
                continue
            # need another arrow at this interval's end
            arrows += 1
            arrow_pos = e
        return arrows