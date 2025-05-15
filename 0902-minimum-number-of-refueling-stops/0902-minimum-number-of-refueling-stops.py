from typing import List
import heapq

class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        max_heap = []
        fuel = startFuel
        prev = 0
        i = 0
        refuels = 0

        while fuel < target:
            # Push all reachable stations into the heap
            while i < len(stations) and stations[i][0] <= fuel:
                # Use negative for max-heap
                heapq.heappush(max_heap, -stations[i][1])
                i += 1

            # If no fuel stations to use and can't reach target
            if not max_heap:
                return -1

            # Refuel with the largest available
            fuel += -heapq.heappop(max_heap)
            refuels += 1

        return refuels
