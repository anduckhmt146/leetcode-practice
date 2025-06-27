# from collections import Counter
# import heapq

# class Solution:
#     def leastInterval(self, tasks, n):
#         tasksCount = Counter(tasks)
#         min_least_time = 0
        
#         maxHeap = [-count for count in tasksCount.values()]
#         heapq.heapify(maxHeap)
        
#         while maxHeap:
#             temp = []
#             steps = 0
            
#             for _ in range(n + 1):
#                 if maxHeap:
#                     cnt = heapq.heappop(maxHeap)
#                     if cnt + 1 < 0:
#                         temp.append(cnt + 1)
#                     steps += 1
#                 elif temp:
#                     steps += 1
            
#             # Push remaining (cooldown) tasks back into the heap
#             for item in temp:
#                 heapq.heappush(maxHeap, item)
            
#             min_least_time += steps if maxHeap else len(temp) + steps
        
#         return min_least_time

from collections import Counter
import heapq

class Solution:
    def leastInterval(self, tasks, n):
        tasksCount = Counter(tasks)
        maxHeap = [-count for count in tasksCount.values()]
        heapq.heapify(maxHeap)
        process_time = 0

        while maxHeap:
            coolDownTasks = []
            steps = 0
            # Each cycle
            for _ in range(n + 1):
                if maxHeap:
                    max_workload_jobs = heapq.heappop(maxHeap)
                    if max_workload_jobs + 1 < 0:
                        coolDownTasks.append(max_workload_jobs + 1)
                    steps += 1
                elif coolDownTasks:
                    # idle jobs
                    steps += 1
            
            for remaining_task in coolDownTasks:
                heapq.heappush(maxHeap, remaining_task)

            process_time += steps
            if not maxHeap and len(coolDownTasks) > 0:
                process_time += len(coolDownTasks)
        

        return process_time
            
                    
            