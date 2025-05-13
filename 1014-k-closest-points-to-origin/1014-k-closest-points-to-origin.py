import heapq
import math
from typing import List

class Solution:
    def distance(self, point: List[int]) -> float:
        return point[0] ** 2 + point[1] ** 2  # skip sqrt for efficiency

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Use a max-heap (invert distances)
        max_heap = []

        for point in points:
            dist = -self.distance(point)  # invert to simulate max-heap
            heapq.heappush(max_heap, (dist, point))

            if len(max_heap) > k:
                # IDEA: Python's heapq is a min-heap by default, meaning:
                # IDEA: It always keeps the smallest element at the top (heap[0]), here is dist
                heapq.heappop(max_heap)

        # Extract only the points from the heap
        return [point for _, point in max_heap]
