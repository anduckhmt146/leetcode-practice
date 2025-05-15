import heapq
from typing import List

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # Pair up capital and profit
        projects = list(zip(capital, profits))
        # Sort by capital needed ascending
        projects.sort()

        max_heap = []
        i = 0
        n = len(profits)

        for _ in range(k):
            # Push all projects we can afford into max-heap
            while i < n and projects[i][0] <= w:
                # Use negative profit because heapq is min-heap
                heapq.heappush(max_heap, -projects[i][1])
                i += 1

            # If no available projects, break
            if not max_heap:
                break

            # Choose the most profitable project
            w += -heapq.heappop(max_heap)

        return w
