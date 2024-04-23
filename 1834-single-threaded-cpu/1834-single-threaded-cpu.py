class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # Sorted tasks by enqueue time
        tasks = sorted([(t[0], t[1], i) for i, t in enumerate(tasks)])
        
        # Heap
        result, heap = [], []

        # Start variable to count push to heap
        cur_task_index = 0

        # Start time
        cur_time = tasks[0][0]

        while len(result) < len(tasks):
            # It ensure push the first task first
            while (cur_task_index < len(tasks)) and (tasks[cur_task_index][0] <= cur_time):
                # Only push process_time and index to heap
                heapq.heappush(heap, (tasks[cur_task_index][1], tasks[cur_task_index][2]))
                cur_task_index += 1
            if heap:
                time_difference, original_index = heapq.heappop(heap)
                cur_time += time_difference
                result.append(original_index)
            # [[5,2],[7,2],[9,4],[6,3],[5,10],[1,1]]
            elif cur_task_index < len(tasks):
                cur_time = tasks[cur_task_index][0]
        return result
            

