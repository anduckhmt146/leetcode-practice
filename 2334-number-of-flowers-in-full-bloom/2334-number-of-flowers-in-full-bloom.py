from typing import List
import bisect

class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        starts = sorted(f[0] for f in flowers)
        ends = sorted(f[1] for f in flowers)
        
        result = []
        for t in people:
            # Flowers that started blooming on or before t
            started = bisect.bisect_right(starts, t)
            # Flowers that ended before t (not blooming at t)
            ended = bisect.bisect_left(ends, t)
            result.append(started - ended)
        
        return result
