from typing import List
from collections import Counter
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counts = Counter(tasks)
    
        # Max heap: use negative counts because heapq is a min-heap
        max_heap = [-cnt for cnt in task_counts.values()]
        heapq.heapify(max_heap)

        time = 0
        while max_heap:
            temp = []
            cycle = 0

            # Try to execute up to n + 1 tasks in one cycle
            for _ in range(n + 1):
                if max_heap:
                    cnt = heapq.heappop(max_heap)
                    if cnt + 1 < 0:
                        temp.append(cnt + 1)  # Task not finished
                    cycle += 1
                elif temp:
                    cycle += 1  # Idle time

            # Push unfinished tasks back into the heap
            for item in temp:
                heapq.heappush(max_heap, item)

            # If heap is empty, only count actual time used (no trailing idles)
            time += cycle if max_heap else len(temp) + cycle

        return time