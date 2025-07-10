from typing import List
from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)

        # Count the frequency of each task
        task_counts = Counter(tasks)

        # Max heap to store tasks by their frequency
        max_heap = [-count for count in task_counts.values()]
        heapq.heapify(max_heap)

        # Queue to manage the cooldown (task, available_time)
        cooldown = deque()
        time = 0

        while max_heap or cooldown:
            time += 1

            if max_heap:
                cnt = heapq.heappop(max_heap) + 1  # do the task
                if cnt != 0:
                    cooldown.append((cnt, time + n))  # add to cooldown

            # Check if any task can come out of cooldown
            if cooldown and cooldown[0][1] == time:
                heapq.heappush(max_heap, cooldown.popleft()[0])

        return time
