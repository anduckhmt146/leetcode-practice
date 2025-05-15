from typing import List
from collections import Counter
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counts = Counter(tasks)
        # Max heap by pushing negative frequencies
        max_heap = [-cnt for cnt in task_counts.values()]
        heapq.heapify(max_heap)

        time = 0

        while max_heap:
            temp = []
            for _ in range(n + 1):
                if max_heap:
                    cnt = heapq.heappop(max_heap)
                    if cnt < -1:
                        temp.append(cnt + 1)  # reduce frequency
                time += 1
                if not max_heap and not temp:
                    break  # all tasks done

            for item in temp:
                heapq.heappush(max_heap, item)

        return time
