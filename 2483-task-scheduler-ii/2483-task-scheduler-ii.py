from typing import List

class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        last_day = {}  # task -> last executed day
        day = 0
        
        for task in tasks:
            day += 1
            if task in last_day and day - last_day[task] <= space:
                # If task was executed too recently, jump forward
                day = last_day[task] + space + 1
            last_day[task] = day
        
        return day
