import heapq
from collections import Counter, deque
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Count the frequency of tasks
        freq = Counter(tasks)
        
        # Python's heapq is a min-heap, so we store negative frequencies for max-heap behavior
        max_heap = [-cnt for cnt in freq.values()]
        heapq.heapify(max_heap)
        
        # Queue to manage cooldowns: (ready_time, -task_count)
        cooldown = deque()
        
        time = 0
        while max_heap or cooldown:
            time += 1
            
            # Release from cooldown if task is ready
            if cooldown and cooldown[0][0] == time:
                heapq.heappush(max_heap, cooldown.popleft()[1])
            
            if max_heap:
                cnt = heapq.heappop(max_heap)
                if cnt + 1 < 0:
                    # Add to cooldown queue with ready time = now + n + 1
                    cooldown.append((time + n + 1, cnt + 1))
        
        return time
