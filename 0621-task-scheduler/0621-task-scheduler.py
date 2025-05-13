from collections import Counter, deque

class Solution:
    def leastInterval(self, tasks, n):
        time = 0
        task_counts = Counter(tasks)
        cooldown = {}  # task -> next available time

        while task_counts:
            available = [task for task in task_counts if cooldown.get(task, 0) <= time]

            if available:
                # Choose task with highest remaining count
                task = max(available, key=lambda x: task_counts[x])
                task_counts[task] -= 1
                if task_counts[task] == 0:
                    del task_counts[task]
                cooldown[task] = time + n + 1

            time += 1

        return time
