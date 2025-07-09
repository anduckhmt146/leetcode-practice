import heapq

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # Sort tasks
        tasks = [(task[0], task[1], idx) for idx, task in enumerate(tasks)]
        tasks.sort(key=lambda x:(x[0], x[1]))

        i = 0
        n = len(tasks)
        process_tasks = []
        curr_time = 0
        res = []

        # Add tasks to queue
        while i < n or process_tasks:
            while i < n and curr_time >= tasks[i][0]:
                heapq.heappush(process_tasks, (tasks[i][1], tasks[i][2])) # (process_time, idx)
                i += 1

            if process_tasks:
                # Process
                process_time, idx = heapq.heappop(process_tasks)
                curr_time += process_time
                res.append(idx)
            else:
                curr_time = tasks[i][0]

        return res