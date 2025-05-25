from typing import List
import heapq

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # Create events: (x, height, start/end)
        events = []
        for left, right, height in buildings:
            events.append((left, -height, right))  # start event; height negated to make max-heap using min-heap
            events.append((right, 0, 0))  # end event

        # Sort by x, then by height
        events.sort()

        result = []
        # Heap of active buildings: (neg_height, end)
        heap = [(0, float('inf'))]  # dummy building with height 0 to avoid empty heap
        prev_max = 0

        for x, neg_height, right in events:
            # Remove buildings from heap that ended before or at x
            while heap and heap[0][1] <= x:
                heapq.heappop(heap)

            if neg_height != 0:
                # Add building height and end to heap
                heapq.heappush(heap, (neg_height, right))

            current_max = -heap[0][0] if heap else 0

            if current_max != prev_max:
                result.append([x, current_max])
                prev_max = current_max

        return result
