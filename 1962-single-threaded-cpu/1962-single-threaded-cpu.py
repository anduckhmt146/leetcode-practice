import heapq
from typing import List

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # Step 1: Add original index and sort tasks by start_time, then execute_time
        tasks = [(task[0], task[1], i) for i, task in enumerate(tasks)]  # (start_time, process_time, index)
        tasks.sort(key=lambda x: (x[0], x[1]))  # Sort by start_time, then process_time

        waiting_tasks = []
        res = []
        i = 0
        n = len(tasks)
        time = 0

        while i < n or waiting_tasks:
            # Push all tasks available at current time into the heap
            while i < n and tasks[i][0] <= time:
                heapq.heappush(waiting_tasks, (tasks[i][1], tasks[i][2]))  # (process_time, index)
                i += 1

            if waiting_tasks:
                process_time, index = heapq.heappop(waiting_tasks)
                time += process_time
                res.append(index)
            else:
                time = tasks[i][0]

        return res
