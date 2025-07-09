import heapq

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # Sort tasks
        tasks = [(task[0], task[1], idx) for idx, task in enumerate(tasks)]
        tasks.sort(key=lambda x:(x[0]))

        running_tasks = []

        # Need a curr_time
        curr_time = tasks[0][0]

        # Index
        i = 0
        n = len(tasks)

        # Result
        result = []

        while i < n or running_tasks:
            # Add to queue
            while i < n and tasks[i][0] <= curr_time:
                process_time, idx = tasks[i][1], tasks[i][2]
                heapq.heappush(running_tasks, (process_time, idx))
                i += 1

            # Process
            if running_tasks:
                process_time, idx = heapq.heappop(running_tasks)
                curr_time += process_time
                result.append(idx)
            else:
                curr_time = tasks[i][0]

        return result
            

