from typing import List

class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        # Cross product of OA and OB vectors
        def cross(o, a, b):
            return (a[0]-o[0])*(b[1]-o[1]) - (a[1]-o[1])*(b[0]-o[0])
        
        # Sort points
        points = sorted(trees)
        if len(points) <= 3:
            return points
        
        # Build lower hull
        lower = []
        for p in points:
            while len(lower) >= 2 and cross(lower[-2], lower[-1], p) < 0:
                lower.pop()
            lower.append(p)
        
        # Build upper hull
        upper = []
        for p in reversed(points):
            while len(upper) >= 2 and cross(upper[-2], upper[-1], p) < 0:
                upper.pop()
            upper.append(p)
        
        # Concatenate lower and upper hull to get full hull
        # Remove duplicates by converting to set then back to list
        hull = lower[:-1] + upper[:-1]
        return list(map(list, set(map(tuple, hull))))
