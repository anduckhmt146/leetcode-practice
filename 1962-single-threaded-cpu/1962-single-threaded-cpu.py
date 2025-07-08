class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # Sort tasks
        tasks = [(task[0], task[1], i) for i, task in enumerate(tasks)]
        tasks.sort(key=lambda x:(x[0], x[1]))

        waiting_task = []
        i = 0
        result = []
        curr_time = 0
        
        while i < len(tasks) or waiting_task:
            # Add to heap
            while i < len(tasks) and tasks[i][0] <= curr_time:
                heapq.heappush(waiting_task, (tasks[i][1], tasks[i][2])) # (end_time, index)
                i += 1

            # Process
            if waiting_task:
                process_time, idx = heapq.heappop(waiting_task)
                curr_time += process_time
                result.append(idx)
            else:
                curr_time = tasks[i][0]

        return result



        