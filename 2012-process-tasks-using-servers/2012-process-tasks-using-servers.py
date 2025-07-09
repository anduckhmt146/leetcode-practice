from typing import List
import heapq

class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        n = len(servers)
        time = 0
        result = []

        # Min-heap for available servers: (weight, index)
        available = [(weight, i) for i, weight in enumerate(servers)]
        heapq.heapify(available)

        # Min-heap for busy servers: (free_time, weight, index)
        busy = []

        for i, task_time in enumerate(tasks):
            time = max(time, i)

            # Release servers that have finished by current time
            while busy and busy[0][0] <= time:
                free_time, weight, index = heapq.heappop(busy)
                heapq.heappush(available, (weight, index))

            if available:
                weight, index = heapq.heappop(available)
                heapq.heappush(busy, (time + task_time, weight, index))
                result.append(index)
            else:
                # No server available now, advance time to earliest free server
                free_time, weight, index = heapq.heappop(busy)
                time = free_time
                heapq.heappush(busy, (time + task_time, weight, index))
                result.append(index)

        return result
